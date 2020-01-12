from setuptools import find_packages, setup
from gunicorn import __version__


setup(
    name='app',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
