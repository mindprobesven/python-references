import json

# some JSON
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

# convert form python to JSON
# a python dict
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)
print(y) # the result is a JSON

# example
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
        "children": ("Ann","Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
}

print(json.dumps(x))
