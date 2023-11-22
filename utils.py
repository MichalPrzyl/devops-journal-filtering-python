import json


def write_to_file(data):
    with open('data3.json', 'w') as json_file:
        json_file.write(json.dumps(data))