import setuptools

from {{ project_name }} import __version__

setuptools.setup(
    name='{{ project_name }}',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'Django',
        'django-debug-toolbar',
        'django-dynamic-fixture',
        'django-extensions',
        # 'django-hosts',
        'django-master-password',
        'django-nose',
        'django-reversion',
        # 'django-suit',
        'django-supervisor',
        'django-webtest',
        'docutils',
        'easy_thumbnails',
        'gunicorn',
        'ipdb',
        'ipython',
        'Jinja2',
        'mkdocs',
        'nose-progressive',
        'pytz',
        'raven',
        'tox',
        'WebTest',
        'Werkzeug',
    ],
)
