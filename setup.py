from {{ project_name }} import __version__
import setuptools

setuptools.setup(
    name='{{ project_name }}',
    version=__version__,
    packages=setuptools.find_packages()
)
