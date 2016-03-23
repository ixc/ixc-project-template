from django.conf import settings
from whitenoise.django import get_path_from_url
from whitenoise.middleware import WhiteNoiseMiddleware


class WhiteNoiseMediaMiddleware(WhiteNoiseMiddleware):
    """
    Serve media as well as static files.
    """

    def __init__(self, *args, **kwargs):
        super(WhiteNoiseMediaMiddleware, self).__init__(*args, **kwargs)
        self.media_prefix = get_path_from_url(
            getattr(settings, 'MEDIA_URL', ''))
        self.media_root = getattr(settings, 'MEDIA_ROOT', None)
        if self.media_root:
            self.add_files(self.media_root, prefix=self.media_prefix)
