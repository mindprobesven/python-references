import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename, 'r') as f:
    numbers_loaded = json.load(f)

print(numbers_loaded)
