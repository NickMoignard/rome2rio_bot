README.txt

A Travel Search Chatbot in Python 3.5

Goal: Build a simplistic chatbot that is intergrated within Slack and accesses/ parses information from the rome2rio.com travel search api.

example:
	hey mate! im new to english. sorry X(
	pls format you question like so!

	... from somewhere to somewhere?

	How do i get from Paris to Nice?

	There are many ways to travel from Paris to Nice!
	would you like the fastest, cheapest or most luxorious option?

	FASTEST!

	ok.

	you xyz, then xyz, then xyz ..

	hope that helps! Would you like me to always assume you want the FASTEST travel option?


Design:
	Parse free text input
		use regular expression to extract, origin and destination
		the string "from x to y?"
		with regx
		r"from (?P<origin>[\w\s]+) to (?P<destination>[\w\s]+)\?"

		gives
		x = origin
		y = destination

	perfom travel search query using rome2rio
		http://www.rome2rio.com/documentation/search
		search api:
			"Provides a simple XML/JSON interface for adding multi-modal search capability to your website, app or service. reurns train, bus, ferry, air, driving and walking routes between any two points. Inputs may be specified either as textual place names or latitude/longitude co-ordinates"

	generate conversational response




