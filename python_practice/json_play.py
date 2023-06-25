import json

# json object
myObject = '{"name":"addy","age":3,"city/town":"sharon","state":"MA"}'

# parse json 
y = json.loads(myObject)

# print name
print(y["name"])

# create a dict
myDict = {
    "name": "izzy",
    "age": 5,
    "city/town": "sharon",
    "state": "MA"
}

toJson = json.dumps(myDict)

print(toJson)

print(len(myDict))