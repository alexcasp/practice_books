import json

filename = 'lknum.json'

with open(filename) as f:
    numbers = json.load(f)
    for i in numbers:
        print('*'.join(i))

# print(f'I know this number, this: {numbers}')