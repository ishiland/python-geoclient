.. python-geoclient documentation master file, created by
   sphinx-quickstart on Thu Jan 17 15:07:02 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python-Geoclient
=================

A python wrapper for calling the RESTful `NYC Geoclient API`_.

.. _NYC Geoclient API: http://developer.cityofnewyork.us/api/geoclient-api-beta

Release v\ |version|.

The NYC Geoclient API provides accurate geocoding for New York City.  It
supports lookups based off of address, BBL, BIN, blockface, intersection, place name and ability to search with an un-parsed
location string. It also provides informative error messages in cases where the geocoding fails.

.. _nyc_geoclient: https://github.com/talos/nyc-geoclient

Whats New?
----------
This library is an updated and maintained fork of `nyc_geoclient`_. It has been updated with the following features:

 - Python 3 compatibility
 - `Geoclient` ``search`` method
 - Optional configuration file
 - Optional `proxies` argument
 - Error handling


Installation
------------

To use the library, you must first obtain your own unique `App` and `Id` key from the NYC Developer Portal. Once you have those credentials,
you can install by simply running:

``$ pip install python-geoclient``

or you can clone the github_ repo and run:

``$ python setup.py install``

.. _github: https://github.com/ishiland/python-geoclient

Contents
--------

.. toctree::
   :maxdepth: 2

   API
   proxy
   config
   errors


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
