import json
from pprint import pprint

file = open('my_json_data','a')

data = """
        Need and Types of Maintenance, Software Configuration Management (SCM), Software Change Management, Version Control, Change control and Reporting, Program Comprehension Techniques, Re-engineering, Reverse Engineering, Tool Support.  
Project Management Concepts, Feasilibility Analysis, Project and Process Planning, Resources Allocations, Software efforts, Schedule, and Cost estimations, Project Scheduling and Tracking, Risk Assessment and Mitigation, Software Quality Assurance (SQA). Project Plan, Project Metrics.
"""

data = data.replace('\n',' ').strip()
data = data.replace('.', ',').strip()
data = data.split(',')

count = 1

mydict = {}

for x in data:
	mydict[count] = {}
	mydict[count]["content"] = x
	mydict[count]["done"] = False
	count += 1

file.write(json.dumps(mydict) + '\n\n\n')
file.close()

pprint(mydict)
