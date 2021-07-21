import os
import pickle as pk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

path=os.getcwd()

dihedrals=[]
filenames=[]
pkfiles = [files for files in os.listdir() if os.path.splitext(files)[1]=='.pickle']
for files in pkfiles: 
    with open(files,'rb') as pkfile:
        current_filename=os.path.splitext(files)[0]
        temporary = pk.load(pkfile)
        for el in temporary:
            if current_filename not in filenames:
                filenames.append(current_filename)
            else:
                filenames.append('')
        dihedrals.extend(temporary)
print(len(dihedrals))

print(len(dihedrals[0]))
print(len(dihedrals[2]))
print(len(dihedrals[4]))

print(filenames)
labels=filenames
colors=['b','b','r','r','g','g']
redundant=[]
plt.hist([dihedrals[0][0:6805],dihedrals[1][0:6805],dihedrals[2],dihedrals[3],dihedrals[4][0:6805],dihedrals[5][0:6805]],10, color = colors, label=labels, alpha=0.5)
    #plt.hist([dihedrals[i]],20, color = colors[i], label=labels[i] if colors[i] not in redundant else '' , alpha=0.5)
plt.xlim([0,180])
plt.legend(loc='upper right')
plt.show()
