"""
Root HOSTconf for ``{{ project_name }}`` project.

See: https://github.com/jezdez/django-hosts
"""

from django_hosts import host, patterns

host_patterns = patterns(
    '',
    host(r'www', '{{ project_name }}.urls', name='www'),
    # host(r'foo', '{{ project_name }}.urls.foo', name='foo'),
)
