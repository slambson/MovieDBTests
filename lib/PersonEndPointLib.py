from HTTPLib import HTTPLib

class PersonEndPointLib:

    def __init__(self, api_key):
        self.api_key = api_key
        self.end_point = "person"
        self.http_lib = HTTPLib(api_key)

    def get_person(self, person_id, api_key=None):
        response = self.http_lib.get("{}/{}".format(self.end_point, person_id), api_key=api_key)
        return response