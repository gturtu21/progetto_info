import pytraj as pt


def triazol_dihedral(traj, time_averaged=True, save_to_file=True, plot=True):
    """ 
    - return a python array of the dihedral angle value
    as a function of simulation timesteps;

    - the angle must be defined as a string with the Amber syntax:
    ':1@O3 :1@C13 :1@C10 :1@C9' ;

    - if more than one angle is present, a list of strings
    should be given as an input.

    """
    import numpy as np

    mymask = traj.get_angle_mask(['O3','C13','C10','C9'])
    dihedrals= pt.dihedral(traj, mask=mymask)
    
    if traj.ndendr > 1:
        media_t = np.zeros((traj.n_frames-1, traj.ndendr))
        for j in range(traj.ndendr):
            for i in range(traj.n_frames):
                if dihedrals[j,i] < 0:
                    dihedrals[j,i]*= -1 
                if i==0:
                    media_t[i,j] = dihedrals[j,0]
                if i==traj.n_frames:
                    pass
                else:
                    media_t[i-1,j] = sum(dihedrals[j,0:i+1])/(i+1) 
        return dihedrals, media_t
    
    media_t = np.zeros((traj.n_frames-1, 1))
    for i in range(traj.n_frames):
        if dihedrals[i] < 0:
            dihedrals[i] *= -1
        if i==0:
            media_t[i,0]=dihedrals[0]
        if i==traj.n_frames:
            pass
        else:
            media_t[i-1,0] = sum(dihedrals[0:i+1])/(i+1) 
    
    return dihedrals, media_t



def CCC_angle(traj):
    """ return a python array with the values of the angle defined
        by atoms C30-C16-C33 (as shown in the sketch below)
        as a function of simulation timesteps """
        ##################################
        #                                #
        #          '''  '''  '''         #
        #           '    '    '          #
        #            '   '   '           #
        #             '  '  '            #
        #              ' ' '             #
        #               '''              #
        #                '               #
        #                '               #
        #                '               #
        #                '               #
        #                '               #
        #              (C16)             #
        #               ' '              #
        #              '   '             #
        #             '     '            #
        #          (C30)   (C33)         #
        #           ' '     ' '          #
        #          '   '   '   '         #
        ##################################
    import numpy as np
    mymask = traj.get_angle_mask(['C30','C16','C33'])
    #mymask = [':'+str(resid)+'@C30'+' :'+str(resid)+'@C16'+' :' +str(resid)+'@C33' for resid in range(1,traj.ndendr+1)]
    angles = pt.angle(traj,mymask)

    #if traj.ndendr > 1:
    media_t = np.zeros((traj.n_frames-1,traj.ndendr))
    for j in range(traj.ndendr):
        for i in range(1,traj.n_frames):
            if traj.ndendr > 1:
                media_t[i-1,j]=sum(angles[j,0:i+1])/(i+1) 
            else:
                media_t[i-1,j]=sum(angles[0:i+1])/(i+1)
    return angles, media_t











