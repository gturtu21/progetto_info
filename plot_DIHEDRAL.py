import pickle as pk
import matplotlib.pyplot as plt

def load_pickle(filename):
    with open(filename, 'rb') as current_file:
        data = pk.load(current_file)
    return data


