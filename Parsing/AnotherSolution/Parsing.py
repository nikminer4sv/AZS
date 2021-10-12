import overpy 
import json

#url = "https://overpass-api.de/api/interpreter?[out:json];{{geocodeArea:Belarus}}->.searchArea;(node[amenity=fuel](area.searchArea);>;);out;"

api = overpy.Overpass()

result = api.query("""[out:json];area(3600059065)->.searchArea;(node[amenity=fuel](area.searchArea);>;);out;""")

counter = 0

JSONResult = list()

for node in result.nodes:

	lat = node.lat
	lng = node.lon
	name = node.tags.get("name", "n/a")
	brand = node.tags.get("brand", "n/a")

	element = {
		'lat' : str(lat),
		'lng' : str(lng),
		'brand' : brand,
		'label' : name
	}
	
	JSONResult.append(element)

result = "[\n"

for element in JSONResult:
	result += str(element) + ',\n'

result = result[:len(result) - 2] + '\n]'

file = open("Data.txt", "w")

file.write(result)

file.close()

#json.dump(JSONResult, open('output.json', 'w'))
