from urllib import parse, request
import json

class Rome2Rio_Search_API():
	""" Rome2Rio_Search_API will handle all interaction with the R2R api
	"""
	def __init__(self, api_key, version=1.4):
		""" synopsis: set users api_key and create a base URL
			input(s): users api key a string,
				(optional) the api version an integer
		"""
		self._key = api_key

 		server = "free.rome2rio.com",
		endpoint = "/api/{}/json/Search".format(version)
		self._baseURL = "http://{}{}".format(server, endpoint)

	def create_search_url(self, origin, destination):
		""" name: create_search_url()
			synopsis: build a search query url specific to rome2rio api
			input(s): the place of origin and the destination as strings
			output(s): the complete search url, a string
		"""
		params = {
					"key": self._key, "oName": origin, "dName": destination,
					"noPath": 1
		}
		encoded_params = urllib.parse.urlencode(params)
		return self._baseURL += "?" + encoded_params

	def perform_r2r_search(self, origin, destination):
		""" name: perform_r2r_search()
			synopsis: get rome2rio.com (R2R) json travel information
			input(s): the place of origin and the destination as strings
			output(s): a dictionary of the information provided by R2R
		"""
		url = self.create_search_url(origin, destination)
		response = response.urlopen(url).read()
		data = json.loads(response)
		return data

