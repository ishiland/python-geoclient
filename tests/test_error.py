from .testcase import TestCase
from .mock_responses import msg_equal, msg_unequal, msg_single
from geoclient.error import GeoclientError

try:
    from unittest import mock  # python 3
except ImportError:
    import mock  # python 2


@mock.patch('geoclient.requests.get')
class TestResponseError(TestCase):
    """
    Tests for bad responses from the Geoclient API
    """

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
    """
    Tests for formatting, no key:values and de-duplication of Geoclient return messages.
    """

    def test_error_msg_equal(self, fake_get):
        # test for two equal messages - 'message' and 'message2'
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = msg_equal

        with self.assertRaises(GeoclientError) as cm:
            self.geoclient.address(
                houseNumber='125',
                street='Worth St',
                borough='Mn',
            )

        self.assertEqual(
            "'WORT ST' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.",
            str(cm.exception)
        )

    def test_error_msg_unequal(self, fake_get):
        # test for two unequal messages - 'message' and 'message2'
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = msg_unequal

        with self.assertRaises(GeoclientError) as cm:
            self.geoclient.address(
                houseNumber='125',
                street='Worth St',
                borough='Mn',
            )
        self.assertEqual(
            "THIS IS THE FIRST MESSAGE. THIS IS THE SECOND MESSAGE",
            str(cm.exception)
        )

    def test_error_msg_single(self, fake_get):
        # test for a single message value - 'message'
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = msg_single

        with self.assertRaises(GeoclientError) as cm:
            self.geoclient.address(
                houseNumber='125',
                street='Worth St',
                borough='Mn',
            )
        self.assertEqual(
            "'WORT ST' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.",
            str(cm.exception)
        )

    def test_error_return_empty(self, fake_get):
        # test for no returned key:values
        fake_get.return_value.status_code = 200
        fake_get.return_value.json.return_value = {u'address': {}}

        with self.assertRaises(GeoclientError) as cm:
            self.geoclient.address(
                houseNumber='125',
                street='Worth St',
                borough='Mn',
            )
        self.assertEqual(
            str(cm.exception),
            "No 'geosupportReturnCode' received from server."
        )
