#Приветствие по заранее созданному имени

import json
filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f'Wellcome back, {username}')
