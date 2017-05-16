import requests

class HTTPLib:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def get(self, end_point, params=None):
        """
        Get the specified end_point using the specified params.  The api_key param will be included in the GET automatically.

        :param end_point: The end point to GET
        :type end_point: String
        :param params: The params to append to the GET
        :type params: dict
        :return:
        """
        url = "{}/{}".format(self.base_url, end_point)
        parameters = {"api_key":self.api_key}
        if params is not None:
            parameters = parameters.update(params)
        response = requests.get(url, params=parameters)
        return response