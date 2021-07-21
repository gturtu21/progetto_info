import os
import numpy as np
from numpy import linalg as LA
import pickle as pk
import matplotlib.pyplot as plt
from savefig import savetoSVG

def DiagonalizeTensor():
    
    """ Extract the 3 components of the RoG tensor """
    
    pickle_files = [files for files in os.listdir() if os.path.splitext(files)[1]=='.pickle' \
            if 'RoGTensor' in os.path.splitext(files)[0]]
    
    for files in pickle_files:
        with open(files,'rb') as pickle_file:
            content = pk.load(pickle_file)
            vector_RoG, tensor_RoG = content
            total_timesteps = np.shape(tensor_RoG)[0]
            eigenvalues = np.zeros((3, total_timesteps))
            for ts in range(total_timesteps):
                F=np.array([[tensor_RoG[ts,0], tensor_RoG[ts,3], tensor_RoG[ts,4]],
                        [tensor_RoG[ts,3], tensor_RoG[ts,1], tensor_RoG[ts,5]],
                        [tensor_RoG[ts,4], tensor_RoG[ts,5], tensor_RoG[ts,2]]])
                eigenvalues[:,ts]=LA.eigh(F)[0]
    return eigenvalues 

def plot_RoG():
    pass
def plot_RoG_components(order):
    pass

egvl=DiagonalizeTensor()
plt.plot(egvl[0])
plt.plot(egvl[1])
plt.plot(egvl[2])
plt.show()
