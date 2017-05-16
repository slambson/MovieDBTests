import unittest
from HTTPLib import HTTPLib
import ConfigParser
import os

class PersonTests(unittest.TestCase):

    def setUp(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config', 'default.ini'))
        api_key_config = config.get("movie_db", "api_v3_key")
        self.http_lib = HTTPLib(api_key_config)

    def test_01_get_person_details(self):
        response = self.http_lib.get("person/221581")
        self.assertTrue(response.status_code == 200)