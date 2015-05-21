import setuptools

from {{ project_name }} import __version__

setuptools.setup(
    name='{{ project_name }}',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'Django',
        'django-extensions',
        'django-fluent-contents[markup,oembeditem,text]',  # code,disquscommentsarea,formdesignerlink,twitterfeed
        'django-fluent-pages[flatpage,fluentpage,redirectnode]',
        'django-fluent-dashboard',
        # 'django-hosts',
        'django-master-password',
        'django-reversion',
        # 'django-suit',
        'django-supervisor',
        'docutils',
        'easy_thumbnails',
        'gunicorn',
        'Jinja2',
        'pytz',
        'raven',
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
        'test': [
            'coverage',
            'django-dynamic-fixture',
            'django-nose',
            'django-webtest',
            'nose-progressive',
            'tox',
            'WebTest',
        ],
    },
)
