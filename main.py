import os
import sys
import numpy as np
import pytraj as pt
import matplotlib.pyplot as plt
import pickle 
from save_to_pickle import SaveToPickle

############
try:
    sys.path.remove('/usr/local/amber16/lib/python2.7/site-packages')
    from mpi4py import MPI
except ValueError:
    print('The path variable was already correct!!')
    pass

comm=MPI.COMM_WORLD

################################# IMPORT THE TRAJECTORY ##################################

class my_traj(pt.TrajectoryIterator):
    """ cosolvent should be 'ETN' or 'TFN' or None """
    from mytrajectories import get_trajectory_files
    all_trajectories = get_trajectory_files()
    def __init__(self, trajectory_index, cosolvent, number_of_dendrons, concentration,timerange=[(0,-2)]):
        self.filepath, self.filetraj, self.filetop = self.all_trajectories[trajectory_index] 
        self.index = trajectory_index+1
        self.cosolvent = cosolvent
        self.ndendr = number_of_dendrons
        self.conc = str(concentration)+'%'
        self.time = timerange
        """ the following command it's used to instantiate a pt.TrajectoryIterator object:
        https://amber-md.github.io/pytraj/latest/_api/pytraj.trajectory_iterator.html"""
        super().__init__(self.filepath+self.filetraj,self.filepath+self.filetop)

    ################

    def get_OH_hydrogens_atomnames(self):
        """ return a list of the atom names of hydrogens in the -OH groups
        present in the dendrons, this method is called to compute distances """
        return [atoms.name for atoms in self.top.atoms if atoms.resid==0 if atoms.type=='ho']
    
    def get_fluorine_atomnames(self,resnumber):
        """ return a list of the atom names of fluorine atoms
        present in the dendrons, this method is called to compute distances """
        return [{'name':atom.name,'resid':atom.resid+1} for atom in self.top.atoms if atom.type=='f' if atom.resid==resnumber]

    def __str__(self):
        if self.cosolvent == None:
            traj_name = 'Trajectory with '+ str(self.ndendr) + ' dendrons in water'
        else:    
            traj_name = 'Trajectory with '+ str(self.ndendr) + ' dendrons in ' + self.cosolvent + self.conc
        return traj_name

    def _filename(self, prefix):
        if self.cosolvent == None:
            suffix = '_traj_' + str(self.ndendr) + 'dendrons_WAT' 
        else:
            suffix = '_traj_' + str(self.ndendr) + 'dendrons_' + self.cosolvent + self.conc
        try:
            full_name = prefix + suffix
        except TypeError:
            print('Argument is not a string, it must be so.')
        return full_name


    #### AVAILABLE ANALYSIS IMPLEMENTED FOR THIS CLASS 

    def radius_of_gyration(self):
        from compute_ROG import radius_of_gyration
        results = radius_of_gyration(self,dimer=True)
        filename = self._filename('RoGTensor')
        SaveToPickle(results,filename)
        return 

    def extract_dihedral(self):
        """ return the value of the angle and the time averaged value 
        index0: angle, index1: angle media"""
        from compute_ANGLES import triazol_dihedral
        results = triazol_dihedral(self)
        filename=(self._filename('Dihedral') , self._filename('Dihedral_media'))
        SaveToPickle(results[0],filename[0])  
        SaveToPickle(results[1],filename[1])
        return

    def extract_CCC_angle(self):
        from compute_ANGLES import CCC_angle
        results = CCC_angle(self)
        filename=(self._filename('AngleCCC'), self._filename('AngleCCC_media'))
        SaveToPickle(results[0],filename[0])
        SaveToPickle(results[1],filename[1])
        return

    def extract_rdf(self, couples='all'):
        from compute_RDF import all_rdf
        if couples=='all':
            results=all_rdf(self)
            filename= self._filename('RDF')
            SaveToPickle(results, filename)
        return 

    def extract_ff_distances(self):
        from compute_DISTANCES import FF_distances
        results = FF_distances(self)
        filename = self._filename('FF_distances') 
        try:
            SaveToPickle(results,filename)
        except ValueError:
            print('This method is available just for trajectory with more than one dendron')
        return 

    def extract_c_ho_distances(self):
        from compute_DISTANCES import CH_distances
        results = CH_distances(self)
        filename = self._filename('CH_distances')
        SaveToPickle(results, filename)
        return 

    def extract_dend_dend_distance(self):
        from compute_DISTANCES import DD_distance
        results = DD_distance(self)
        filename = self._filename('DD_distance')
        SaveToPickle(results, filename)

    def average_structure(self):
        """ Compute the Root Mean Square Displacement of each dendron using
            the starting point as reference structure """
        #return pt.mean_structure(self,mask=':'+str(dendron_id), frame_indices=None)
        #return pt.rmsf(self,mask=':'+str(dendron_id), frame_indices=None)
        results = []
        filename = self._filename('RMSD')
        for dendrons in range(1,self.ndendr+1):
            results.append(pt.rmsd(self,mask=':'+str(dendrons), frame_indices=None))
            SaveToPickle(results, filename)
        return

    ####### THIS METHOD PERFORMS ALL THE ANALYSIS LISTED ABOVE

    def all_analysis(self):
        import time
        start = time.time()
        self.radius_of_gyration()
        print('ROG analysis: Done')
        self.extract_dihedral()
        print('Dihedral analysis: Done')
        self.extract_rdf()
        print('RDF analysis: Done')
        self.extract_ff_distances()
        print('FF distances: Done')
        self.extract_c_ho_distances()
        print('C-ho distances: Done')
        end = time.time()
        print('Total time of execution: ', end-start)
        return 

