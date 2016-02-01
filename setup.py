import setuptools

setuptools.setup(
    name='{{ project_name }}',
    use_scm_version={'version_scheme': 'post-release'},
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'deployo',
        # 'django-any-urlfield',  # Optional integration with `django-fluent-contents`
        'django-compressor<1.6',  # See: https://github.com/django-compressor/django-compressor/issues/706
        'django-dynamic-fixture',
        'django-extensions',
        'django-flat-theme<1.1.3',  # See: https://github.com/elky/django-flat-theme/issues/30
        'django-fluent-contents[markup,oembeditem,text]<1.1',  # See: https://github.com/edoburu/django-fluent-contents/issues/67
        'django-fluent-dashboard',
        'django-fluent-pages[flatpage,fluentpage,redirectnode]',
        'django-generic',
        # 'django-glamkit',
        # 'django-hosts',
        # 'django-icekit[brightcove,forms,search]',
        'django-master-password',
        'django-model-settings',
        'django-multiurl',
        'django-nose',
        'django-polymorphic-auth',
        'django-post-office-trigger',
        'django-reversion',
        'django-supervisor',
        'django-test-without-migrations',
        'django-timezone',
        'django-webtest',
        'Django>=1.7,<1.8',  # 1.8 is untested with ICEkit
        'docutils',
        'easy_thumbnails',
        'gunicorn',
        # 'icekit-notifications',
        'Jinja2',
        'nose-progressive',
        'pytz',
        'raven',
        'WebTest',

        # Override incompatible versions for nested dependencies.
        'django-mptt<0.8',  # 0.8 Backwards incompatible. See: https://github.com/django-mptt/django-mptt/releases
        'django-polymorphic<0.8',  # Backwards incompatible. See: https://django-polymorphic.readthedocs.org/en/latest/changelog.html#version-0-8-2015-12-28
    ],
    extras_require={
        'dev': [
            'django-debug-toolbar',
            'glamkit-fallbackserve',
            'ipdb',
            'ipython',
            'mkdocs',
            'Werkzeug',
        ],
        'postgres': ['psycopg2'],
    },
    setup_requires=['setuptools_scm'],
)
