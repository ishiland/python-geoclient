from .testcase import TestCase
from .mock_responses import *

try:
    from unittest import mock  # python 3
except ImportError:
    import mock  # python 2


@mock.patch('geoclient.requests.get')
class TestApi(TestCase):
    def test_address(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = address_response

        result = self.geoclient.address(
            houseNumber='125',
            street='Worth St',
            borough='Mn',
        )
        self.assertDictSubsetEqual({
            'bblBoroughCode': '1',
            'boePreferredStreetName': 'WORTH STREET',
            'houseNumber': '125'
        }, result)

    def test_address_zip(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = address_zip_response

        result = self.geoclient.address_zip(
            houseNumber='125',
            street='Worth St',
            zip='10013',
        )
        self.assertDictSubsetEqual({
            'zipCodeIn': '10013',
            'boePreferredStreetName': 'WORTH STREET',
            'houseNumber': '125'
        }, result)

    def test_bbl(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = bbl_response

        result = self.geoclient.bbl(
            borough='1',
            block='00168',
            lot='0032',
        )
        self.assertDictSubsetEqual({
            'bblBoroughCode': '1',
            'bblTaxBlock': '00168',
            'bblTaxLot': '0032'
        }, result)

    def test_bin(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = bin_response

        result = self.geoclient.bin(
            bin='1001831'
        )
        self.assertDictSubsetEqual({
            'bblTaxBlock': '00168',
            'bblTaxLot': '0032',
            'buildingIdentificationNumber': '1001831'
        }, result)

    def test_blockface(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = blockface_response

        result = self.geoclient.blockface(
            onStreet='Lafayette St',
            crossStreetOne='Worth st',
            crossStreetTwo='Leonard St',
            borough='MN'
        )

        self.assertDictSubsetEqual({
            'firstStreetNameNormalized': 'LAFAYETTE STREET',
            'secondStreetNameNormalized': 'WORTH STREET',
        }, result)

    def test_intersection(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = intersection_response

        result = self.geoclient.intersection(
            crossStreetOne='Worth St',
            crossStreetTwo='Centre St',
            borough='MN'
        )

        self.assertDictSubsetEqual({
            'lionNodeNumber': '0015490',
            'numberOfIntersectingStreets': '2',
        }, result)

    def test_place(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = place_response

        result = self.geoclient.place(
            name='Empire State Building',
            borough='MN'
        )

        self.assertDictSubsetEqual({
            'boePreferredStreetName': 'EMPIRE STATE BUILDING',
            'message': '350 5 AVENUE IS THE UNDERLYING ADDRESS OF EMPIRE STATE BUILDING',
        }, result)

    def test_search(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = search_response

        result = self.geoclient.search(
            'Empire State Building'
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['level'], '1')
        self.assertEqual(result[0]['status'], 'POSSIBLE_MATCH')
        self.assertEqual(result[0]['request'], 'place [name=Empire State Building, borough=MANHATTAN, zip=null]')
        self.assertEqual(result[0]['response']['message'],
                         '350 5 AVENUE IS THE UNDERLYING ADDRESS OF EMPIRE STATE BUILDING')

    def test_search_no_result(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = {u'results': []}

        result = self.geoclient.search(
            'THIS VALUE RETURNS NO RESULT'
        )
        self.assertEqual(len(result), 0)
