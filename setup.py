try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )

extras = {'dev': []}

try:
    from unittest import mock
except ImportError:
    extras['dev'].append('mock') # need to use mock for unit testing on python 2.7

try:
    from nyc_geoclient.config import __version__
except ImportError:
    print('config import error')
    exec(open("nyc_geoclient/config.py").read())

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = ['nyc_geoclient']
setup(
    name='nyc_geoclient',
    version=__version__,
    description='Python bindings for the NYC Geoclient REST API',
    long_description=long_description,
    author='John Krauss',
    author_email='john@accursedware.com',
    url='http://github.com/talos/nyc-geoclient',
    packages=packages,
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'requests>=2.21.0'
    ],
    test_suite="tests",
    extras_require=extras
)
