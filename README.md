# NYC Geoclient Python Bindings
Python bindings for the REST [NYC Geoclient API][api].

 [![Python 2.7 | 3.3+](https://img.shields.io/badge/python-2.7%20%7C%203.3+-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Build Status](https://travis-ci.org/ishiland/nyc-geoclient.svg?branch=master)](https://travis-ci.org/ishiland/nyc-geoclient)  [![PyPI version](https://img.shields.io/pypi/v/nyc_geoclient.svg)](https://pypi.python.org/pypi/nyc_geoclient/)

  [api]: http://developer.cityofnewyork.us/api/geoclient-api-beta

### Whats New

 - Python 3 support
 - Single Field Search
 - Optional proxy argument
 - Optional configuration file to store api credentials and proxy configuration

### Usage

First, you will need to register an application with the [NYC Developer
Portal][portal], and make sure that you check off access to the Geoclient API
for the application.  Take note of the Application's ID and key.  You will not
be able to use the ID and key until [DoITT][] approves you -- this could take
several days, and you will receive an email when this happens.  There isn't any
indication of your status on the dashboard, but all requests will return a 403.

  [portal]: https://developer.cityofnewyork.us/
  [DoITT]: http://www.nyc.gov/html/doitt/html/home/home.shtml

You can `pip install` nyc-geoclient.  It depends upon the [requests][] library.

  [requests]: http://docs.python-requests.org/en/latest/index.html
```sh
$ pip install nyc_geoclient
```

Once your app has been approved by DoITT, using the API is simple:

```python
>>> from nyc_geoclient import Geoclient
>>> g = Geoclient('my app ID', 'my app key')
```

You can also add an optional `proxies` argument:

```python
>>> proxies = {
        'http': 'http://user:password@host:port',
        'https': 'http://user:password@host:port',
    }
>>> g = Geoclient('my app ID', 'my app key', proxies)
```

Alternatively, store api credentials and proxy settings in a single configuration file. `nyc_geoclient` will look for a file called `.nyc-developer.ini` in your home directory. If on a windows machine, this directory is typically located in `C:\Users\<MY-USERNAME>\`. A sample  `.nyc-developer.ini` looks like this:
```Ini
[GEOCLIENT]
id = my-app-id
key = my-app-key

[PROXIES]
http = http://user:password@host:port
https = http://user:password@host:port
```

All of the REST endpoints are supported.
```python
>>> g.address('1500', 'Madison Ave', 'Manhattan')
{u'assemblyDistrict': u'68',
 u'boardOfElectionsPreferredLgc': u'1',
 u'boePreferredStreetName': u'MADISON AVENUE',
 u'boePreferredstreetCode': u'12539001',
 u'boroughCode1In': u'1',
 u'censusBlock2000': u'2000',
 u'censusBlock2010': u'3003',
 u'censusTract1990': u' 168  ',
 u'censusTract2000': u' 168  ',
 u'censusTract2010': u' 168  ',
 u'cityCouncilDistrict': u'08',
 u'civilCourtDistrict': u'06',
 u'coincidentSegmentCount': u'1',
...

>>> g.intersection('atlantic ave', 'nevins st', 'Brooklyn')
{u'assemblyDistrict': u'52',
 u'boroughCode1In': u'3',
 u'censusTract1990': u'  39  ',
 u'censusTract2000': u'  39  ',
 u'censusTract2010': u'  39  ',
 u'cityCouncilDistrict': u'33',
 u'civilCourtDistrict': u'01',
 u'communityDistrict': u'302',
 u'communityDistrictBoroughCode': u'3',
 u'communityDistrictNumber': u'02',
 u'communitySchoolDistrict': u'15',
 u'congressionalDistrict': u'08',
 u'crossStreetNamesFlagIn': u'E',
 u'dcpPreferredLgcForStreet1': u'01',
 u'dcpPreferredLgcForStreet2': u'01',
 u'dotStreetLightContractorArea': u'3',
...
```
##### Errors

In cases where the geocoder does not work, it will still return a dict.  You
must look at the value for `message` to see what happened.
```python
     >>> g.intersection('atlantic ave', 'nevins st', 'manhattan')
     {u'boroughCode1In': u'1',
     u'censusTract1990': u'      ',
     u'censusTract2000': u'      ',
     u'censusTract2010': u'      ',
     u'crossStreetNamesFlagIn': u'E',
     u'firstBoroughName': u'MANHATTAN',
     u'firstStreetNameNormalized': u'ATLANTIC AVENUE',
     u'geosupportFunctionCode': u'2',
     u'geosupportReturnCode': u'11',
     u'message': u"'ATLANTIC AVE' NOT RECOGNIZED. THERE ARE NO SIMILAR NAMES",
     u'secondStreetNameNormalized': u'NEVINS ST',
     u'streetName1In': u'ATLANTIC AVE',
     u'streetName2In': u'NEVINS ST',
     u'workAreaFormatIndicatorIn': u'C'}
```
The messages are generally very helpful.

### Documentation

Take a look at the [Python documentation][] for details on using the bindings,
which closely follows the [DoITT documentation][] (requires account/login).

  [Python documentation]: https://nyc-geoclient.readthedocs.org/
  [DoITT documentation]: http://developer.cityofnewyork.us/api/geoclient-api-beta

### Tests

run `python setup.py test`

### License

BSD.
