#    The function returns the list containing all the path to possible trajectories : 
#    - 0: Two fdg3 in ETN 5%;            # instantiate as my_traj(0, 'ETN', 2, 5, 0, -2)
#    - 1: One fdg3 in ETN 5% ;           # instantiate as my_traj(1, 'ETN', 1, 5, 0, -2)
#    - 2: One fdg3 in WATER;             # instantiate as my_traj(2,  None, 1, 0, 0, -2)
#    - 3: Two fdg3 in TFN (0-100 ns) ;   # instantiate as my_traj(3, 'TFN', 2, 5, 0, -2)
#    - 4: Two fdg3 in TFN (100-200 ns) ; # instantiate as my_traj(4, 'TFN', 2, 5, 0, -2)
#    - 5: Two fdg3 in TFN (0-200 ns);    # instantiate as my_traj(5, 'TFN', 2, 5, 0, -2)
#    - 6: Two fdg3 in ETN (0-200 ns);    # instantiate as my_traj(6, 'ETN', 2, 5, 0, -2)
#    - 7: One fdg3 in TFN 5%        ;    # instantiate as my_traj(7, 'TFN', 1, 5, 0, -2)
#    - 8: One fdg3 in ETN 25%       ;    # instantiate as my_traj(8, 'ETN', 1, 25, 0, -2)
#    - 9: Two fdg3 in ETN 25%       ;    # instantiate as my_traj(9, 'ETN', 2, 25, 0, -2)
import pytraj as pt
import matplotlib.pyplot as plt
from main import my_traj
import time
import os
import multiprocessing
#os.environ["OPENBLAS_NUM_THREADS"] = "1" # export OPENBLAS_NUM_THREADS=1

start=time.time()

mynewtraj=my_traj(5,'TFN', 2, 5, 0, 500)
mynewtraj.extract_dihedral()
#mynewtraj.extract_ff_distances()
#mynewtraj.all_analysis()


end=time.time()
output=open('out.txt','w')

output.write('Total time:' + str((end-start)/60) +'min.')
