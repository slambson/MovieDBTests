import unittest
from PersonEndPointLib import PersonEndPointLib
import ConfigParser
import os
import json

class PersonTests(unittest.TestCase):

    def setUp(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config', 'default.ini'))
        api_key_config = config.get("movie_db", "api_v3_key")
        self.person_endpoint_lib = PersonEndPointLib(api_key_config)

    def test_01_get_person_details_valid_key(self):
        response = self.person_endpoint_lib.get_person("221581")
        self.assertTrue(response.status_code == 200)

    def test_02_get_person_details_invalid_key(self):
        response = self.person_endpoint_lib.get_person("221581", api_key="111111")
        self.assertTrue(response.status_code == 401)
        self.assertTrue(response.reason == "Unauthorized")
        response_text = json.loads(response.text)
        self.assertTrue(response_text["status_code"] == 7)
        self.assertTrue(response_text["status_message"] == "Invalid API key: You must be granted a valid key.")