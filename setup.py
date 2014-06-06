from {{ project_name }} import VERSION
import setuptools

setuptools.setup(
    name='{{ project_name }}',
    version=VERSION,
    packages=setuptools.find_packages()
)
