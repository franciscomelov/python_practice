import json

input = '''[
    {"id" : "001",
    "x" : "2",
    "name": "Chuck"
    },
    {"id" : "009",
    "x" : "7",
    "name": "Chuck"
    }
]
'''

info = json.loads(input)
print(f'User count: {len(info)}')

for item in info:
    print(f'Name: {item["name"]}')
    print(f'Id: {item["id"]}')
    print(f'Attribute: {item["x"]}')