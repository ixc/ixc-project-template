"""
Work around a few ``WhiteNoise`` feature limitations:

  * Serve media as well as static files.
  * Save media with hashed filenames, so they can be cached forever by a CDN.
  * Do not crash the ``collectstatic`` management command when a referenced
    file is not found or has an unknown scheme.

"""

from __future__ import absolute_import

import hashlib
import logging
import posixpath
import re

from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import default_storage, FileSystemStorage
from django.utils.six.moves.urllib.parse import urlparse
from whitenoise.middleware import WhiteNoiseMiddleware
from whitenoise.storage import \
    CompressedManifestStaticFilesStorage, MissingFileError
from whitenoise.utils import ensure_leading_trailing_slash

logger = logging.getLogger(__name__)


class CustomCompressedManifestStaticFilesStorage(
        CompressedManifestStaticFilesStorage):

    # Log a warning instead of raising an exception when a referenced file is
    # not found. These are often in 3rd party packages and outside our control.
    def make_helpful_exception(self, exception, name):
        exception = super(CustomCompressedManifestStaticFilesStorage, self) \
            .make_helpful_exception(exception, name)
        if isinstance(exception, MissingFileError):
            logger.warning('\n\nWARNING: %s' % exception)
            return False
        return exception

    # Don't try to rewrite URLs with unknown schemes.
    def url_converter(self, name, template=None):
        converter = super(CustomCompressedManifestStaticFilesStorage, self) \
            .url_converter(name, template)

        def custom_converter(matchobj):
            matched, url = matchobj.groups()
            if re.match(r'(?i)([a-z]+://|//|#|data:)', url):
                return matched
            return converter(matchobj)

        return custom_converter


# Serve media as well as static files.
class WhiteNoiseMediaMiddleware(WhiteNoiseMiddleware):

    config_attrs = WhiteNoiseMiddleware.config_attrs + ('media_prefix', )
    media_prefix = None

    def __init__(self, *args, **kwargs):
        super(WhiteNoiseMediaMiddleware, self).__init__(*args, **kwargs)
        if self.media_root:
            self.add_files(self.media_root, prefix=self.media_prefix)

    def check_settings(self, settings):
        super(WhiteNoiseMediaMiddleware, self).check_settings(settings)
        if self.media_prefix == '/':
            media_url = getattr(settings, 'MEDIA_URL', '').rstrip('/')
            raise ImproperlyConfigured(
                'MEDIA_URL setting must include a path component, for '
                'example: MEDIA_URL = {0!r}'.format(media_url + '/media/')
            )

    def configure_from_settings(self, settings):
        self.media_prefix = urlparse(settings.MEDIA_URL or '').path
        super(WhiteNoiseMediaMiddleware, self).configure_from_settings(settings)
        self.media_prefix = ensure_leading_trailing_slash(self.media_prefix)
        self.media_root = settings.MEDIA_ROOT

    # Media with hashed filenames are always immutable.
    def is_immutable_file(self, path, url):
        if super(WhiteNoiseMediaMiddleware, self).is_immutable_file(path, url):
            return True
        if isinstance(default_storage, HashedMediaStorage) and \
                url.startswith(self.media_prefix):
            return True
        return False


# Save media with hashed filenames, so they can be cached forever by a CDN.
class HashedMediaStorage(FileSystemStorage):

    # Disable Django's name conflict resolution.
    def get_available_name(self, name):
        return name

    def _save(self, name, content):
        # Get hash from content.
        md5 = hashlib.md5()
        for chunk in content.chunks():
            md5.update(chunk)
        file_hash = md5.hexdigest()[:12]

        # Add hash to name.
        name, ext = posixpath.splitext(name)
        name = '%s.%s%s' % (name, file_hash, ext)

        # Overwrite existing file, because it must have the same content.
        if self.exists(name):
            self.delete(name)

        return super(HashedMediaStorage, self)._save(name, content)
