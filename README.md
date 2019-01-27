# Python-Geoclient
Call the RESTful [NYC Geoclient API](http://developer.cityofnewyork.us/api/geoclient-api-beta) using python.

 [![Python 2.7 | 3.4+](https://img.shields.io/badge/python-2.7%20%7C%203.4+-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Build Status](https://travis-ci.org/ishiland/python-geoclient.svg?branch=master)](https://travis-ci.org/ishiland/python-geoclient)  [![PyPI version](https://img.shields.io/pypi/v/python-geoclient.svg)](https://pypi.python.org/pypi/python-geoclient/)

### Introduction

This library provides a Python interface for using the [NYC Geoclient API](http://developer.cityofnewyork.us/api/geoclient-api-beta). It is an updated and maintained fork of [nyc_geoclient](https://github.com/talos/nyc-geoclient).

In order to use the library, you must first register an application with the [NYC Developer Portal](https://developer.cityofnewyork.us/) to obtain an application key and ID.


### Installing
you can install python-geoclient using:

`$ pip install python-geoclient`

or you can clone this directory and:

`$ python setup.py install`

### Quickstart
Once your app has been registered with [DoITT](http://www.nyc.gov/html/doitt/html/home/home.shtml), using the API is simple:

```python
from geoclient import Geoclient
g = Geoclient('my app ID', 'my app key')
```


You can use any of the available methods documented in the [API](https://python-geoclient.readthedocs.io/en/latest/API.html):
```python
g.address(100, 'Gold st', 'MN')

{u'uspsPreferredCityName': u'NEW YORK',
 u'fireCompanyType': u'E',
 u'fromLionNodeId': u'0015445',
 u'cooperativeIdNumber': u'0000',
 u'dotStreetLightContractorArea': u'1',
 u'lionBoroughCodeForVanityAddress': u'1',
 u'zipCode': u'10038',
 u'fireCompanyNumber': u'006',
 u'communityDistrict': u'101',
 u'firstStreetNameNormalized': u'GOLD STREET',
 u'boroughCode1In': u'1',
 u'latitude': 40.71035225065372,
 u'longitude': -74.00400739046181,
 ...
 }
```

### Geocoding Errors

python-geoclient will raise a `GeoclientError` when the Geoclient API returns an error code. Sometimes there is more information returned, in which case the exception will have a `result` dictionary.

```python
from geoclient import GeoclientError
try:
    g.address(125, 'wort st', 1)
except GeoclientError as e:
    print(e) # 'WORT STREET' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.
    print(e.result['streetName1']) # WORTH SQUARE
```

### Documentation

The [Python Geoclient documentation][] details using the library.

The API closely follows the [DoITT documentation][] (requires account/login).

  [Python Geoclient documentation]: https://python-geoclient.readthedocs.org/
  [DoITT documentation]: http://developer.cityofnewyork.us/api/geoclient-api-beta

### Running Tests

`python setup.py test`

### Contributing

If you see an issue or would like to contribute, pull requests are welcome.

### License

BSD.
