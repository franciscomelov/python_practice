import json

data = '''{
    "name": "Chuck",
    "phone": {
        "type": "int1",
        "number": "+1 743 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)

print(f'Name: {info["name"]}')
print(f'Hide: {info["email"]["hide"]}')