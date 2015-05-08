import json
from pprint import pprint

file = open('my_json_data','a')

data = '''
	Tractable and Untractable Problems:
P, NP, NP complete and NP hard problems, examples of these problems like satisfy
ability problems, vertex cover problem, Hamiltonian path problem, traveling sales man
'''

data = data.replace('\n',' ').strip()
data = data.split(',')

count = 1

mydict = {}

for x in data:
	mydict[count] = {}
	mydict[count]["content"] = x
	mydict[count]["done"] = False
	count += 1

file.write(json.dumps(mydict) + '\n\n\n')

pprint(mydict)
