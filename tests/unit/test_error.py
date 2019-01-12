from ..testcase import TestCase
from nyc_geoclient.error import GeoclientError

try:
    from unittest import mock  # python 3
except ImportError:
    import mock  # python 2


@mock.patch('nyc_geoclient.requests.get')
class TestError(TestCase):
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
