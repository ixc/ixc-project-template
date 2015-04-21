import setuptools

from {{ project_name }} import __version__

setuptools.setup(
    name='{{ project_name }}',
    version=__version__,
    packages=setuptools.find_packages()
)
