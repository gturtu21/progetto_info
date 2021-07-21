import numpy as np

filename='angolo_conc25_tfe_par20'
angle = np.loadtxt(filename+'.txt')

counter=[0,]*9
delta=20
for _ in angle[:,1]:
    if _ >= 0 and _ < delta:
        counter[0]+=1
    if _ >=delta and _ < delta*2:
        counter[1]+=1
    if _ >=delta*2 and _< delta*3:
        counter[2]+=1
    if _ >=delta*3 and _< delta*4:
        counter[3]+=1
    if _ >=delta*4 and _< delta*5:
        counter[4]+=1
    if _ >=delta*5 and _< delta*6:
        counter[5]+=1
    if _ >=delta*6 and _< delta*7:
        counter[6]+=1
    if _ >=delta*7 and _< delta*8:
        counter[7]+=1
    if _ >=delta*8 and _<= delta*9:
        counter[8]+=1

import matplotlib.pyplot as plt

angoli=range(0,180,20)

plt.hist(angle[:,1],20,color='r')
plt.xlabel('Angle(degrees)',fontsize=15)
plt.xlim([0,180])
plt.ylim([0,200])
plt.ylabel('Counts',fontsize=15)
plt.tick_params(width=2)
plt.savefig(filename+'.png',format='png')
#plt.show()



