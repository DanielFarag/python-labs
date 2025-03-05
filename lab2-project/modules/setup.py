import os
import json

def start():
    db_file = 'db.json'

    if os.path.exists(db_file):
        with open(db_file, 'r') as file:
            data = json.load(file)
            if 'auth' in data and 'users' in data and 'projects' in data:
                pass
            else:
                raise Exception('File is corrupted')
    else:
        data = {
            'auth': {},
            'users': [],
            'projects': []
        }
        with open(db_file, 'w') as file:
            json.dump(data, file, indent=4)
