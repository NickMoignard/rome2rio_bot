import re
from urllib import parse, request
import json


class Travel_ChatBot(Natural_Language):

	def __init__(self, api_key):

		api = Rome2Rio_Search_API(api_key)
		self._query_exp = r"from (?P<origin>[\w\s]+) to (?P<destination>[\w\s]+)\?"

	def natural_language_search(query):
		success = re.search(self._query_exp, text)
		if (success):
			data = api.perform_r2r_search(
											success.group("origin"),
											success.group("destination")
			)
			return self.journey_description(data)
		else:
			return """Sorry, i did not understand your query!
					try and format your question like:
						from x to y?"""


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



class Natural_Language_Building():
	""" Natural_Language will handle all the Construction of natural language 
		from data aquired from the rome2rio.com api
	"""

	def get_verb(vehicle_kind):
		""" name: get_verb()
			synopsis: gets a verb from a mode of transport
			input(s): vehicle_kind, a string
			output(s): a verb, string
		"""
		if vehicle_kind == "plane": 
			return "fly"
		elif vehicle_kind == "car": 
			return "drive"
		else:
			return "take the {}".format(vehicle_kind)

	def route_description(data, route_index):
		""" name: route_description()
			synopsis: create a description of a journey
			input(s): route_index, an integer
			output(s): description of a journey, a string
		"""
		route = data["routes"][route_index]
		step_count = len(route["segments"])
		steps = [
			step_description(data, route_index, i) for i in range(steps_count)
		]
		description = ", then".join(steps)
		return description

	def step_description(data, route_index, step_index):
		""" name: step_description()
			synopsis: create a description of a step in a journey
			input(s): the route_index, an integer
				step_index, an integer
			output(s): step description, a string
		"""
		step_template = "{verb} from {origin} to {destination}"

		step = data["routes"][route_index]["segments"][step_index]
		arriveAt = data["places"][step["arrPlace"]]["shortName"]

		departFrom = data["places"][step["depPlace"]]["shortName"]
		verb = get_verb(data["vehicles"][segment["vehicle"]]["kind"])

		return step_template.format(
									verb=verb, origin=departFrom,
									destination=arriveAt
		)



