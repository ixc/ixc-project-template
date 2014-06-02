from {{ project_name }} import VERSION
import setuptools

setuptools.setup(
    name='{{ project_name }}',
    version=VERSION,
    packages=setuptools.find_packages(),
    install_requires=[
        'Django>=1.6.5',
        'django-bower>=5.0.1',
        'django-debug-toolbar>=1.2.1',
        'django-dynamic-fixture>=1.7.0',
        'django-extensions>=1.3.7',
        'django-nose>=1.2',
        'django-reversion>=1.8.1',
        'django-suit>=0.2.8',
        'django-supervisor>=0.3.2',
        'django-webtest>=1.7.7',
        'easy_thumbnails>=2.0.1',
        'gunicorn>=18.0',
        'nose-cov>=1.6',
        'nose-progressive>=1.5.1',
        'pyScss>=1.2.0',
        'pytz>=2014.3',
        'raven>=5.0.0',
        'South>=0.8.4',
        'WebTest>=2.0.15',
    ]
)
