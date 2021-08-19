import pickle
import matplotlib.pyplot as plt

rmsd=[]
for _ in range(1,8):
    with open('rmsd_dendrons_traj_'+str(_)+'.pickle', 'rb') as myfile:
        rmsd.append(pickle.load(myfile))

plt.plot(rmsd[0][0])
plt.plot(rmsd[0][1])
plt.plot(rmsd[4][0])
plt.plot(rmsd[4][1])
plt.show()
