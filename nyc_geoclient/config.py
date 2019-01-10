BASE_URL = u'https://api.cityofnewyork.us/geoclient/v1/'

BOROUGHS = {
    'MANHATTAN': 1, 'MN': 1, 'NEW YORK': 1, 'NY': 1,
    'BRONX': 2, 'THE BRONX': 2, 'BX': 2,
    'BROOKLYN': 3, 'BK': 3, 'BKLYN': 3, 'KINGS': 3,
    'QUEENS': 4, 'QN': 4, 'QU': 4,
    'STATEN ISLAND': 5, 'SI': 5, 'STATEN IS': 5, 'RICHMOND': 5,
    '': '',
}

# store api id & key or proxies in your home directory
USER_CONFIG = '~/.nyc-developer.ini'

__version__ = '0.1.0'

# __build__ = 0x000002