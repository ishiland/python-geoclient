from .testcase import TestCase
from .mock_responses import address_response_error
from geoclient.error import GeoclientError

try:
    from unittest import mock  # python 3
except ImportError:
    import mock  # python 2


@mock.patch('geoclient.requests.get')
class TestResponseError(TestCase):
    def test_403(self, fake_get):
        fake_get.return_value.status_code = 403
        fake_get.return_value.reason = "Forbidden"
        self.assertRaises(GeoclientError, self.geoclient.search, "100 Gold Street")

    def test_Undefined(self, fake_get):
        self.assertRaises(GeoclientError, self.geoclient.search, "100 Gold Street")

    def test_None(self, fake_get):
        fake_get.return_value.status_code = None
        fake_get.return_value.reason = None
        self.assertRaises(GeoclientError, self.geoclient.search, "100 Gold Street")


@mock.patch('geoclient.requests.get')
class TestGeoclientMessageError(TestCase):
    def test_address_error(self, fake_get):
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = address_response_error
        self.assertRaises(GeoclientError, self.geoclient.address, '125', 'Wort st', 1)
