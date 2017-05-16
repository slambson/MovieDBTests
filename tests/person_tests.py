import unittest
from PersonEndPointLib import PersonEndPointLib
import ConfigParser
import os
import json
from testconfig import config

class PersonTests(unittest.TestCase):

    def setUp(self):
        try:
            api_key_config = config['movie_db']['api_v3_key']
            self.person_endpoint_lib = PersonEndPointLib(api_key_config)
        except KeyError as ke:
            print "Failed to retrieve the api key from the config.  Cannot run test!"
            print "Please update the config/default.ini file with a valid API key and pass that config to nose, i.e.: "
            print "nosetests --tc-file=config/default.ini tests/person_tests.py"

    def test_01_get_person_details_valid_key(self):
        """Get Person details with an valid api key

        :author: Sharon Lambson
        :component: Person Endpoint
        :steps:
            1. GET from person endpoint specifying a valid key (and valid person)
        :expectedResults:
            1. Should return a 200 status code
        """
        response = self.person_endpoint_lib.get_person("221581")
        self.assertTrue(response.status_code == 200, "Expected HTTP status_code to be '200'")

    def test_02_get_person_details_invalid_key(self):
        """Get Person details with an invalid api key

        :author: Sharon Lambson
        :component: Person Endpoint
        :steps:
            1. GET from person endpoint specifying an invalid key (and valid person)
        :expectedResults:
            1. Should return a 401 status code, 'Unauthorized' reason, and a descriptive status message
        """
        response = self.person_endpoint_lib.get_person("221581", api_key="111111")
        self.assertTrue(response.status_code == 401, "Expected HTTP status_code to be '401'")
        self.assertEqual(response.reason, "Unauthorized")
        response_text = json.loads(response.text)
        self.validate_response_text(response_text, "status_message", "Invalid API key: You must be granted a valid key.")

    def test_03_invalid_person_details(self):
        """Get Person details with an invalid person id

        :author: Sharon Lambson
        :component: Person Endpoint
        :steps:
            1. GET from person endpoint specifying an invalid person id (and valid key)
        :expectedResults:
            1. Should return a 404 status code, 'Not Found' reason, and a descriptive status message
        """
        response = self.person_endpoint_lib.get_person("99999999")
        self.assertTrue(response.status_code == 404, "Expected HTTP status_code to be '404'")
        self.assertEqual(response.reason, "Not Found")
        response_text = json.loads(response.text)
        self.validate_response_text(response_text, "status_message","The resource you requested could not be found.")

    def test_04_valid_person_details(self):
        """Get Person details with an valid person id

        :author: Sharon Lambson
        :component: Person Endpoint
        :steps:
            1. GET from person endpoint specifying an invalid person id (and valid key)
        :expectedResults:
            1. Should return the correct person details
        """
        response = self.person_endpoint_lib.get_person("221581")
        self.assertTrue(response.status_code == 200, "Expected HTTP status_code to be '200'")
        response_text = json.loads(response.text)
        self.validate_response_text(response_text, "adult", False)
        self.validate_response_text(response_text, "also_known_as", [])
        self.validate_response_text(response_text, "biography", "From Wikipedia, the free encyclopedia Rebel Wilson is an Australian actress, writer, and stand-up comedienne, known for her roles in the television series Pizza and Bogan Pride and the film Bridesmaids. Description above from the Wikipedia article Rebel Wilson, licensed under CC-BY-SA, full list of contributors on Wikipedia.")
        self.validate_response_text(response_text, "birthday", "1980-03-02")
        self.validate_response_text(response_text, "deathday", "")
        self.validate_response_text(response_text, "gender", 1)
        self.validate_response_text(response_text, "homepage", "")
        self.validate_response_text(response_text, "imdb_id", "nm2313103")
        self.validate_response_text(response_text, "name", "Rebel Wilson")
        self.validate_response_text(response_text, "place_of_birth", None)
        self.validate_response_text(response_text, "popularity", 4.151649)
        self.validate_response_text(response_text, "profile_path", "/hwgTgqFLFwTBesbCAKtWa1ARrp7.jpg")

    def validate_response_text(self, response_text, attribute, expected_value):
        """
        Validate the specified response text key exists and has the expected value

        :param response_text: The response text json object
        :type response_text: dict
        :param attribute: The attribute to verify
        :type attribute: str
        :param expected_value: The expected value
        :return:
        """
        self.assertTrue(response_text.has_key(attribute), "The response text does not have the expected key: '{};".format(attribute))
        self.assertEqual(response_text[attribute], expected_value, "The response text attribute '{}' has value: '{}' instead of value: '{}".format(attribute, response_text[attribute], expected_value))
