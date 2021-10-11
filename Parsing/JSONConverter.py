import json

data_file = open('data2.0.txt', 'r')

JSONResult = list()

for line in data_file:
	x, y, z = line.split('] [')
	name = x[1:]
	adress = y
	coords = z[:len(z) - 2]
	element = {
		'Name' : name,
		'Adress' : adress,
		'Coords' : coords.split(',')
	}
	JSONResult.append(element)



print(json.dump(JSONResult, open('file.json', 'w')))