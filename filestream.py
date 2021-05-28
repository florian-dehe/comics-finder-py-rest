import json

# Read data
def read_data_as_json(filepath):
    f = open(filepath, "r")
    data = f.read()
    f.close()
    return json.loads(data)

def write_data_as_json(filepath, data):
    f = open(filepath, "w")
    f.write(json.dumps(data))
    f.close()
