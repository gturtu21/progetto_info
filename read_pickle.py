import sys
import pickle as pk

try:
    file_input = sys.argv[1]
    with open(file_input, 'rb') as current_file:
        data = pk.load(current_file)
except IndexError:
    print('One argument must be given as input')


if type(data) == dict:
    print(type(data))

for _ in data.values():
    print(type(_))




