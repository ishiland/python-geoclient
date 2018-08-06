#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Install prereqs here and now if we can.
    from setuptools import setup
    kw = { 'install_requires': [
        'requests>=2.19.1'
    ] }
except ImportError:
    from distutils.core import setup
    print('No setuptools.  Do\n\n    $ pip install -I requirements.txt\n\n\nto install dependencies.')
    kw = {}

try:
    execfile('nyc_geoclient/version.py')
except NameError:
    exec(open("./nyc_geoclient/version.py").read())

packages = ['nyc_geoclient']
setup(
    name='nyc_geoclient',
    version=__version__,
    description='Python bindings for the NYC Geoclient REST API',
    long_description=open('README.md').read(),
    author='John Krauss',
    author_email='john@accursedware.com',
    url='http://github.com/talos/nyc-geoclient',
    packages=packages,
    license='BSD',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
    **kw
)
