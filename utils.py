import json


def write_to_file(filename, data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data))