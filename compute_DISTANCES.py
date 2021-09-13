import pytraj as pt
import numpy as np

def CH_distances(traj, time_averaged=True, save_to_file=True, plot=True):
    """ return a python array of all the distances between the Carbon-sp3 holding 
    the fluorinated structure (AtomName: 'C') and the 8 hydroxyl groups represented by
    alchoholic hydrogen (AtomType: 'ho') as a function of simulation timesteps """
    import time
    from write_MASK2 import AmbMask, DistMask
    
    my_hydrogens_names = traj.get_OH_atomnames(resnumber=0)
    carbon_sp3 = traj.get_C_atomnames()

    mymask=[DistMask(carbon, hydrog).write() for carbon in carbon_sp3 for hydrog in my_hydrogens_names] 

    distances = pt.distance(traj, mymask)
    distances_dict = {couple:distance for couple in mymask for distance in distances}
    
    return distances_dict

##########################################################################################################

def FF_distances(traj):
    """ return a python array of all the INTER-molecular distances between
    fluorine atoms in the dendrons present in the simulation box"""
    import time
    from write_MASK2 import AmbMask, DistMask
    
    if traj.ndendr < 2:
        return 

    fluor_dend1=traj.get_F_atomnames(resnumber=0)
    fluor_dend2=traj.get_F_atomnames(resnumber=1)
    #mymask = [':'+fluorine1['resid']+'@'+fluorine1['name']+' :'+fluorine2['resid']+'@'+fluorine2['name'] for fluorine1 in fluorine_dendron1 for fluorine2 in fluorine_dendron2]
    mymask = [DistMask(fluor1, fluor2).write() for fluor1 in fluor_dend1 for fluor2 in fluor_dend2]
    distances = pt.distance(traj, mymask)
    distances_dict = {couple:distance for couple in mymask for distance in distances}
    return distances_dict



def DD_distance(traj):
    """ return a python array of the distance between csp3-csp3 of two dendrons """
    import time
    from write_MASK2 import AmbMask, DistMask

    if traj.ndendr < 2:
        return

    #carbons = traj.get_C_atomnames(resnumber=0)
    carbons = traj.get_C_atomnames()
    print(carbons)
    #mymask = [':1@C'+ ' :2@C']

    mymask_with_doubles = [DistMask(carbon1, carbon2).write() for carbon1 in carbons for carbon2 in carbons if carbon1 != carbon2]
    #distmasks = [DistMask(carbon1, carbon2) for carbon1 in carbons for carbon2 in carbons if carbon1 != carbon2]
    #mymask = [distmask.write() for distmask in distmasks]
    mymask = []
    for element in mymask_with_doubles:
        if element not in mymask:
            mymask.append(element)
    print(mymask)
    
    distances = pt.distance(traj, mymask)
    distance_dict = {couple:distance for couple in mask for distance in distances}

    ### the following should be removed now 
    #if traj.ndendr == 2:
    #    distances_dict = {couple:distances for couple in mymask for distance in distances}
    #    return distances_dict
    #distance_dict = {couple:distances}
    return distance_dict

