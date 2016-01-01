import setuptools

from {{ project_name }} import __version__

setuptools.setup(
    name='{{ project_name }}',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'Django',
        'django_compressor',
        'django-dynamic-fixture',
        'django-extensions',
        'django-fluent-contents[markup,oembeditem,text]',  # code,disquscommentsarea,formdesignerlink,twitterfeed
        'django-fluent-dashboard',
        'django-fluent-pages[flatpage,fluentpage,redirectnode]',
        # 'django-frontend-compiler',
        # 'django-hosts',
        # 'django-master-password',
        # 'django-model-settings',
        # 'django-nose',
        # 'django-polymorphic-auth',
        'django-nose',
        'django-reversion',
        'django-supervisor',
        'django-webtest',
        'docutils',
        'easy_thumbnails',
        'gunicorn',
        'Jinja2',
        'nose-progressive',
        'pytz',
        'raven',
        'WebTest',
    ],
    extras_require={
        'dev': [
            'django-debug-toolbar',
            'ipdb',
            'ipython',
            'mkdocs',
            'Werkzeug',
        ],
        'postgres': ['psycopg2'],
    },
)
