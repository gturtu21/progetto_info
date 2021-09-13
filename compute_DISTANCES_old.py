import pytraj as pt
import numpy as np

def CH_distances(traj, time_averaged=True, save_to_file=True, plot=True):
    """ return a python array of all the distances between the Carbon-sp3 holding 
    the fluorinated structure (AtomName: 'C') and the 8 hydroxyl groups represented by
    alchoholic hydrogen (AtomType: 'ho') as a function of simulation timesteps """
    import time
    #print('Start CH_distances')
    
    #my_hydrogens_names= [atoms.name for atoms in traj.top.atoms if atoms.resid==0 if atoms.type=='ho']
    
    my_hydrogens_names=traj.get_OH_atomnames()
    
    
    output = open('output12.txt','w') 
    #### metodo 2
    start = time.time()

    dendron_indeces = range(1, traj.ndendr+1)
    mymask=[':' + str(index) + '@C '+ ' :' + str(index) + '@'+ hydrogens for index in dendron_indeces for hydrogens in my_hydrogens_names]
    distances = pt.distance(traj, mymask)
    #distances_dict = pt.distance(traj, mymask)
    distances_dict = {couple:distance for couple in mymask for distance in distances}
    end = time.time()
    output.write('method2:'+str(end - start))
    return distances_dict

    #### metodo 1 
#    start1 = time.time()
#
#    distances = []
#    if traj.ndendr > 0:
#        for dendrons in range(1,traj.ndendr+1):
#            #print("I'm in dendron"+str(dendrons))
#            mymask=[':'+str(dendrons)+'@C'+ ' :' + str(dendrons) + '@'+ hydrogens for hydrogens in my_hydrogens_names]
#            distances.append(pt.distance(traj, mymask))
#    else:
#        #my_hydrogen_names = [atoms.name for atoms in traj.top.atoms if atoms.resid== 0 if atoms.type=='ho']
#        distances = {}
#        for hydrogen_i in my_hydrogen_names:
#            certain_CH_couple = ':1@C :1@' + hydrogen_i
#            distances[hydrogen_i] = pt.distance(traj, certain_CH_couple)
    
#    end1 = time.time()
#    output.write('method1:'+str(end1-start1))

#    return my_hydrogens_names, distances


##########################################################################################################

def FF_distances(traj):
    """ return a python array of all the INTER-molecular distances between
    fluorine atoms in the dendrons present in the simulation box"""
    if traj.ndendr < 2:
        return 
    fluorine_dendron1=traj.get_F_atomnames(resnumber=0)
    fluorine_dendron2=traj.get_F_atomnames(resnumber=1)
    #fluorine_dendron1=([atom for atom in traj.top.atoms if atom.type=='f' if atom.resid==0])
    #fluorine_dendron2=([atom for atom in traj.top.atoms if atom.type=='f' if atom.resid==1])
    mymask = [':'+str(fluorine1['resid'])+'@'+str(fluorine1['name'])+' :'+str(fluorine2['resid'])+'@'+str(fluorine2['name']) for fluorine1 in fluorine_dendron1 for fluorine2 in fluorine_dendron2]
    distances = pt.distance(traj, mymask)
    distances_dict = {couple:distance for couple in mymask for distance in distances}
    return distances_dict



def DD_distance(traj):
    """ return a python array of the distance between csp3-csp3 of two dendrons """
    if traj.ndendr < 2:
        return
    mymask = [':1@C'+ ' :2@C']
    distance = pt.distance(traj, mymask)
    distances_dict = {couple:distance for couple in mymask for distance in distances}
    return distances_dict
