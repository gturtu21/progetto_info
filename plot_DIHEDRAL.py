import pickle as pk
import matplotlib.pyplot as plt

filename = input('Which file?')

def load_pickle(filename):
    with open(filename, 'rb') as current_file:
        data = pk.load(current_file)
    return data

mydata = load_pickle(filename)
plt.plot(mydata[2])
plt.show()


