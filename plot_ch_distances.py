import pickle
import matplotlib.pyplot as plt


with open('CH_distances_traj1.pickle', 'rb') as myfile:
    distances = pickle.load(myfile)

print(distances[0])


plt.plot(distances[1][0][0])
plt.plot(distances[1][0][1])
plt.show()
