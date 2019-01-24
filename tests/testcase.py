import unittest
from geoclient import Geoclient


class TestCase(unittest.TestCase):
    def assertDictSubsetEqual(self, subset, superset):
        for k, v in subset.items():
            self.assertEqual(v, superset[k], k)

    @classmethod
    def setUpClass(cls):
        cls.geoclient = Geoclient(app_key='my-app-key', app_id='my-app-id')
