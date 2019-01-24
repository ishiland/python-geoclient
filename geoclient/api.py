import os
try:
    from configparser import ConfigParser  # Python 3
except ImportError:
    from ConfigParser import ConfigParser  # Python 2
import requests
from geoclient.config import BASE_URL, USER_CONFIG
from .error import GeoclientError


class Geoclient(object):
    """
    This object's methods provide access to the NYC Geoclient REST API.

    You must have registered an app with the NYC Developer Portal
    (http://developer.cityofnewyork.us/api/geoclient-api-beta), and make sure
    that you check off access to the Geoclient API for the application.  Take
    note of the Application's ID and key.  You will not be able to use the ID
    and key until DoITT approves you. All requests will return a ``403`` until you
    are approved.

    :param app_id:
        Your NYC Geoclient application ID.
    :param app_key:
        Your NYC Geoclient application key.
    :param proxies:
        (optional) A dictionary of proxies.
    """

    BASE_URL = BASE_URL

    def __init__(self, app_id=None, app_key=None, proxies=None):

        config = ConfigParser()
        config.read(os.path.expanduser(USER_CONFIG))

        if (app_id is None or app_key is None) and config.has_section('GEOCLIENT'):
            credentials = dict(config.items('GEOCLIENT'))
            app_id = credentials['id']
            app_key = credentials['key']

        if proxies is None and config.has_section('PROXIES'):
            proxies = dict(config.items('PROXIES'))

        if not app_id:
            raise GeoclientError("Missing app_id")

        if not app_key:
            raise GeoclientError("Missing app_key")

        self.app_id = app_id
        self.app_key = app_key
        self.proxies = proxies

    def _request(self, endpoint, **kwargs):
        kwargs.update({
            'app_id': self.app_id,
            'app_key': self.app_key
        })

        # Ensure no 'None' values are sent to server
        for k in list(kwargs.keys()):
            if kwargs[k] is None:
                kwargs.pop(k)

        key = 'results' if endpoint == "search" else endpoint

        r = requests.get('{}{}'.format(Geoclient.BASE_URL, endpoint),
                         params=kwargs,
                         proxies=self.proxies)

        if r.status_code == requests.codes.ok:
            result = r.json()[key]

            if isinstance(result, dict):
                return_code = result['geosupportReturnCode']
                if not return_code.isdigit() or int(return_code) > 1:
                    raise GeoclientError(
                        result['message'] + ' ' + result['message2'],
                        result
                    )
            return result

        else:
            raise GeoclientError("{} {}".format(r.status_code, r.reason))

    def address(self, houseNumber, street, borough):
        """
        Given a valid address, provides blockface-level, property-level, and
        political information.

        :param houseNumber:
            The house number to look up.
        :param street:
            The name of the street to look up.
        :param borough:
            The borough to look within. Can be a valid Borough name, numeric value (1-5) or common borough abbreviation.

        :returns: A dict with blockface-level, property-level, and political
            information.
        """

        return self._request(u'address', houseNumber=houseNumber, street=street,
                             borough=borough)

    def address_zip(self, houseNumber, street, zip):
        """
        Like the above address function, except it uses "zip code" instead of borough

        :param houseNumber:
            The house number to look up.
        :param street:
            The name of the street to look up
        :param zip:
            The zip code of the address to look up.

        :returns: A dict with blockface-level, property-level, and political
            information.
        """

        return self._request(u'address', houseNumber=houseNumber, street=street, zip=zip)

    def bbl(self, borough, block, lot):
        """
        Given a valid borough, block, and lot provides property-level
        information.

        :param borough:
            The borough to look within. Can be a valid Borough name, numeric value (1-5) or common borough abbreviation.
        :param block:
            The tax block to look up.
        :param lot:
            The tax lot to look up.

        :returns: A dict with property-level information.
        """

        return self._request(u'bbl', borough=borough, block=block, lot=lot)

    def bin(self, bin):
        """
        Given a valid building identification number (BIN) provides
        property-level information.

        :param bin:
            The BIN to look up.

        :returns: A dict with property-level information.
        """

        return self._request(u'bin', bin=bin)

    def blockface(self, onStreet, crossStreetOne, crossStreetTwo, borough,
                  boroughCrossStreetOne=None, boroughCrossStreetTwo=None,
                  compassDirection=None):
        """
        Given a valid borough, "on street" and cross streets provides
        blockface-level information.

        :param onStreet:
            "On street" (street name of target blockface).
        :param crossStreetOne:
            First cross street of blockface.
        :param crossStreetTwo:
            Second cross street of blockface.
        :param borough:
            The borough to look within. Can be a valid Borough name, numeric value (1-5) or common borough abbreviation.
        :param boroughCrossStreetOne:
            (optional) Borough of first cross street. Defaults to value of
            borough parameter if not supplied.
        :param boroughCrossStreetTwo:
            (optional) Borough of second cross street. Defaults to value of
            borough parameter if not supplied.
        :param compassDirection:
            (optional) Used to request information about only one side of the
            street. Valid values are: N, S, E or W.

        :returns: A dict with blockface-level information.
        """

        return self._request(u'blockface', onStreet=onStreet,
                             crossStreetOne=crossStreetOne,
                             crossStreetTwo=crossStreetTwo,
                             borough=borough,
                             boroughCrossStreetOne=boroughCrossStreetOne,
                             boroughCrossStreetTwo=boroughCrossStreetTwo,
                             compassDirection=compassDirection)

    def intersection(self, crossStreetOne, crossStreetTwo, borough,
                     boroughCrossStreetTwo=None, compassDirection=None):
        """
        Given a valid borough and cross streets returns information for the
        point defined by the two streets.

        :param crossStreetOne:
            First cross street
        :param crossStreetTwo:
            Second cross street
        :param borough:
            Borough of first cross street or of all cross streets if no other
            borough parameter is supplied. Can be a valid Borough name, numeric value (1-5) or common borough
            abbreviation.
        :param boroughCrossStreetTwo:
            (optional) Borough of second cross street. If not supplied, assumed
            to be same as borough parameter.  Must be 'Bronx', 'Brooklyn',
            'Manhattan', 'Queens', or 'Staten Island' (case-insensitive).
        :param compassDirection:
            (optional) Optional. for most requests. Required for streets that
            intersect more than once. Valid values are: N, S, E or W.

        :returns: A dict with intersection-level information.
        """

        return self._request(u'intersection', crossStreetOne=crossStreetOne,
                             crossStreetTwo=crossStreetTwo,
                             borough=borough,
                             boroughCrossStreetTwo=boroughCrossStreetTwo,
                             compassDirection=compassDirection)

    def place(self, name, borough):
        """
        Same as 'Address' above using well-known NYC place name for input.

        :param name:
            Place name of well-known NYC location.
        :param borough:
            The borough to look within. Can be a valid Borough name, numeric value (1-5) or common borough abbreviation.

        :returns: A dict with place-level information.
        """

        return self._request(u'place', name=name, borough=borough)

    def search(self,
               input,
               exactMatchForSingleSuccess=None,
               exactMatchMaxLevel=None,
               returnPolicy=None,
               returnPossiblesWithExact=None,
               returnRejections=None,
               returnTokens=None,
               similarNamesDistance=None):
        """
        Beginning with version 1.10, any of the six request types documented in section 1.2 can be accessed using a
        single unparsed location string. Assuming that the Geoclient parser can guess the location type requested and
        the given single-field input parameter contains contains enough information to generate a successful Geosupport
        call, the service will return one or more sets of geocodes corresponding to the type of request that was made.

        :param input:
             Unparsed location input.
        :param exactMatchForSingleSuccess:
            (optional) Whether a search returning only one possible successfully geocoded
            location is considered an exact match. Defaults to false.
        :param exactMatchMaxLevel:
            (optional) The maximum number of sub-search levels to perform if Geosupport
            rejects the input but suggests alternative street names, etc.
            Defaults to 3. Maximum is allowable value is 6.
        :param returnPolicy:
            (optional) Whether to return information on the search policy used to perform the search.
            Defaults to false.
        :param returnPossiblesWithExact:
            (optional) Whether to also return successfully geocoded possible matches
            when available in addition to the exact match. Defaults to false.
        :param returnRejections:
            (optional) Whether to return rejected response data from Geosupport. Defaults to false.
        :param returnTokens:
            (optional) Whether to return the parsed input tokens recognized by the parser. Defaults to false.
        :param similarNamesDistance:
            (optional) Maximum allowable Levenshtein distance between user input
            and a similar name suggestion from Geosupport. Defaults to 8.
            A higher number will allow more "guesses" to be made about an unrecognized street name.

        :returns: List of geocodes corresponding to the type of request that was made.
        """

        return self._request(u'search',
                             input=input,
                             exactMatchForSingleSuccess=exactMatchForSingleSuccess,
                             exactMatchMaxLevel=exactMatchMaxLevel,
                             returnPolicy=returnPolicy,
                             returnPossiblesWithExact=returnPossiblesWithExact,
                             returnRejections=returnRejections,
                             returnTokens=returnTokens,
                             similarNamesDistance=similarNamesDistance)
