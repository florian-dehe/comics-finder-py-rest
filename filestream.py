import json
import os

#Lock File
def check_lock_file(name):
    return os.path.exists(name)

def create_lock_file(name):
    if check_lock_file(name):
        return False
    
    f = open(name, "w")
    f.write("lock")
    f.close()

    return True

def remove_lock_file(name):
    if not check_lock_file(name):
        return False
    
    os.remove(name)

    return True

# Read data
def read_data_as_json(filepath):
    if create_lock_file("lock-"+filepath):
        f = open(filepath, "r")
        data = f.read()
        f.close()
        remove_lock_file("lock-"+filepath)
        return json.loads(data)
    return None

def write_data_as_json(filepath, data):
    if create_lock_file("lock-"+filepath):
        f = open(filepath, "w")
        f.write(json.dumps(data))
        f.close()
        remove_lock_file("lock-"+filepath)
