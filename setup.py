try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )

config = {}

with open("geoclient/config.py") as fp:
    exec (fp.read(), config)

extras = {'dev': []}

try:
    from unittest import mock
except ImportError:
    extras['dev'].append('mock')  # need to use mock for unit testing on python 2.7

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-geoclient',
    version=config['__version__'],
    description='Python wrapper for the NYC Geoclient RESTful API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=config['__author__'],
    author_email='ishiland@gmail.com',
    url='http://github.com/ishiland/python-geoclient',
    packages=['geoclient'],
    license='BSD',
    keywords=['NYC', 'geocoder', 'python-geoclient', 'geoclient'],
    classifiers=[
        'Development Status :: 4 - Beta',
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
