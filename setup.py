import datetime
import os
import setuptools

# Allow installation without git repository, e.g. inside Docker.
if os.path.exists('.git'):
    kwargs = dict(
        use_scm_version={'version_scheme': 'post-release'},
        setup_requires=['setuptools_scm'],
    )
else:
    kwargs = dict(version='0+d'+datetime.date.today().strftime('%Y%m%d'))

setuptools.setup(
    name='{{ project_name }}',
    packages=setuptools.find_packages(),
    install_requires=[
        'celery[redis]',
        'coverage',
        'deployo',
        # 'django-any-urlfield',  # Optional integration with `django-fluent-contents`
        'django-app-namespace-template-loader',
        'django-celery-email',
        'django-compressor',
        'django-dynamic-fixture',
        'django-extensions',
        'django-flat-theme<1.1.3',  # See: https://github.com/elky/django-flat-theme/issues/30
        'django-fluent-contents[markup,oembeditem,text]<1.1',  # See: https://github.com/edoburu/django-fluent-contents/issues/67
        'django-fluent-dashboard',
        'django-fluent-pages[flatpage,fluentpage,redirectnode,reversion]',
        # 'django-guardian',
        # 'django-generic',
        # 'django-glamkit',
        # 'django-hosts',
        # 'django-icekit[brightcove,forms,search]',
        'django-master-password',
        'django-model-settings',
        'django-multiurl',
        'django-nose',
        'django-polymorphic-auth',
        'django-post-office',
        'django-redis',
        'django-reversion>=1.9.3,<1.10',  # 1.9.3+ use DB transactions, 1.10 has breaking changes for Django 1.9
        'django-storages<1.2',  # See: https://github.com/jschneier/django-storages/blob/cf3cb76ca060f0dd82766daa43ee92fccca3dec7/storages/backends/s3boto.py#L28-L30
        'django-supervisor',
        'django-test-without-migrations',
        'django-timezone',
        'django-webtest',
        'Django>=1.8,<1.9',  # LTS
        'docutils',
        'easy_thumbnails',
        'gunicorn',
        # 'icekit-notifications',
        'ixc-redactor',
        'Jinja2',
        'nose-progressive',
        'psycopg2',
        'pytz',
        'raven',
        'WebTest',
        'whitenoise>=3.0',

        # Override incompatible versions for nested dependencies.
        'boto<=2.27',  # See: https://github.com/danilop/yas3fs/issues/26
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
    },
    **kwargs
)
