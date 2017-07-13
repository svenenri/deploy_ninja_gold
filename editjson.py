from os.path import join, dirname
from dotenv import load_dotenv
import os
from collections import OrderedDict # <-- Maintain order of the JSON file
import json

def jsonRead(file):
    with open(file) as output:
        data = json.load(output, object_pairs_hook=OrderedDict)
    return data

def prettyJsonRead(file):
    with open(file) as output:
        data = json.load(output, object_pairs_hook=OrderedDict)
        prettyData = json.dumps(data, indent=4)
        return prettyData

def jsonWrite(file, info):
    with open(file, "w") as output:
		output.seek(0)
		json.dump(info, output, indent = 2)

def jsonAppend(file, info):
	data = jsonRead(file)
	data["containerDefinitions"][0]["image"] = info
	jsonWrite(file, data)


# Path to access the json variables
dotenv_path = join(dirname(__file__), "jsonvars.env.encrypted")
load_dotenv(dotenv_path)


# File path of JSON file from .env file
jsonFile = "webtask.json"

# Add DB value to the JSON file
jsonAppend(jsonFile, os.environ.get("IMAGE"))

# Display JSON file to show injected vars
# print prettyJsonRead(jsonFile)


"""
def pathMaker(*args):
	path = ""
	for arg in args:
		if type(arg) is str:
			path = path + "\"" + arg + "\"]"
		elif type(arg) is int:
			path = path +

pathMaker("containerDefinitions", 0, "environment", 0, "value")
"""
