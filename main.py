import os
import sys
import numpy as np
import pytraj as pt
import matplotlib.pyplot as plt
import pickle 
from save_to_pickle import SaveToPickle
from time_fun import time_fun

class all_trajectories():
    """ This class collects all the paths to the available trajectories
        and shows how to instantiate 'my_traj' class objects using
        the available methods usage(index). For instance:
        - instantiate: alltraj= all_trajectories();
        - list all the trajectories: alltraj.enumerate();
        - choose one trajectory and check how to instantiate it: alltraj.usage(3)."""

    def __init__(self):
        from mytrajectories import trajectory_files, trajectory_description, my_traj_class_usage 
        self.__files__ = trajectory_files()
        self.__commands__ = my_traj_class_usage()
        self.__descriptions__ = trajectory_description()

    def __repr__(self):
        return   """
                   ###################################################################
                   # To show the trajectories available use instancename.enumerate() #
                   ###################################################################
                   """

    def enumerate(self):
        print("""\n This is the list of available trajectories, to check their usage try the method .usage(index) \n """)
        for el in self.__descriptions__:
            print('- Index ' + str(self.__descriptions__.index(el)) + ': ' + el + '\n') 
        
    def usage(self,index):
        return self.__commands__[index]



class my_traj(pt.TrajectoryIterator):
    
    """ This class instantiate trajectory object regarding fluorinated dendrons molecular dynamics simulations.
    - trajectory_index: read 'mytrajectories.py' where all the trajectories are listed with indexes;
    - cosolvent: should be 'ETN' or 'TFN' or None;
    - number_of_dendrons: depends on the simulation box simulated;
    - concentration: it's the concentration of ETN or TFN;
    - first_step: number of step to start loading the simulation;
    - last_step: number of step to stop loading the simulation. """

    ############### IMPORT THE TRAJECTORY ##############
    from write_MASK import AmbMask, DistMask, AngleMask, DihMask
    from mytrajectories import trajectory_files
    all_trajectories = trajectory_files()

    def __init__(self, trajectory_index, cosolvent, number_of_dendrons, concentration, first_step, last_step):
        self.filepath, self.filetraj, self.filetop = self.all_trajectories[trajectory_index] 
        self.index = trajectory_index+1
        self.cosolvent = cosolvent
        self.ndendr = number_of_dendrons
        self.conc = str(concentration)+'%'
        self.timerange = [(first_step, last_step)] ## this syntax is required by the superclass definition

        """ the following command it's used to instantiate a pt.TrajectoryIterator object:
        https://amber-md.github.io/pytraj/latest/_api/pytraj.trajectory_iterator.html """
        super().__init__(self.filepath+self.filetraj, self.filepath+self.filetop, self.timerange)

    ################ Getter Methods ################

    def get_atom_types(self):
        atom_types_dict = {}
        for atom in self.top.atoms:
            if atom.type not in atom_types_dict:
                atom_types_dict[atom.type] = 1
            else:
                atom_types_dict[atom.type] += 1
        return atom_types_dict

    def get_atom_dict(self, atom_type, residue = 'JAN'):
        """ return a dictionary with atom_names and resid_numbers 
        of the given atom type"""
        #### by default this method searches for 'JAN' molecules if any is present 
        
        if type(residue) == str:
            if atom_type in self.get_atom_types():
                return [{'name':atom.name,'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.type == atom_type if atom.resname == residue]  
            atom_name = atom_type
            atom_dict = [{'name':atom.name,'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.name == atom_name if atom.resname == residue]  
            if atom_dict != []:
                return atom_dict
            print('No atom with atom_type/atom_name and resname/resid given is present in the current trajectory')
        
        #### if resnumber is given this method 
        if type(residue) == int:
            if atom_type in self.get_atom_types():
                return [{'name':atom.name,'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.type == atom_type if atom.resid == residue]  
            atom_name = atom_type
            atom_dict = [{'name':atom.name,'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.name == atom_name if atom.resid == residue]  
            if atom_dict != []:
                return atom_dict
            print('First argument passed to get_atom_dict() does not correspond to any AtomType or AtomName in the current trajectory')
        return 

    ### get_OH_atomnames has been rewritten as a call of get_atom_dict
    #def get_OH_atomnames(self, resnumber = 'all'):
    #    """ return a list of the atom names of hydrogens in the -OH groups
    #    present in the dendrons, this method is called to compute distances """
    #    #return [atoms.name for atoms in self.top.atoms if atoms.resid==0 if atoms.type=='ho']   # version1
    #    if resnumber == 'all':
    #        return [{'name':atom.name,'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.type=='ho' if atom.resname=='JAN']
    #    if resnumber < self.ndendr:
    #        return [{'name':atom.name,'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.type=='ho' if atom.resid==resnumber]  
    #    print('resnumber used in get_OH_atomnames() is greater than the number of dendrons:' + str(self.ndendr))
    #    return 
    def get_OH_atomnames(self):
        """ return a list of the atom names of hydrogens in the -OH groups
        present in the dendrons, this method is called to compute distances """
        return self.get_atom_dict('ho')
    #########################################################################################
    #def get_C_atomnames(self,resnumber):
    def get_C_atomnames(self):
        """ return an atom_dict for the atom with name 'C' """
        #return [{'name':atom.name, 'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.name=='C' if atom.resid==resnumber]
        #return [{'name':atom.name, 'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.name=='C' and atom.resname == 'JAN']
        return self.get_atom_dict('C')

    ####  THIS IS THE OLD VERSION OF IT, TRY TO GENERALIZE TO ndendr > 2
    #def get_F_atomnames(self,resnumber):
    #    """ return a list of the atom names of fluorine atoms
    #    present in the dendrons, this method is called to compute distances """
        #return [{'name':atom.name,'resid':str(atom.resid+1)} for atom in self.top.atoms if atom.type=='f' if atom.resid==resnumber]
    def get_F_atomnames(self):  
        return self.get_atom_dict('f')

    def get_angle_mask(self, atom_names):
        """ atom_names is a list or tuple of atom names such as:
            ['C13','C5','N1',C4']
        """
        if len(atom_names) < 3 or len(atom_names) > 4:
            print('A list of 3 or 4 atom names should be given as an input')
            return
        if self.ndendr > 1:
            angle_mask = [' '.join([':' + str(resid) + '@' + atom_name for atom_name in atom_names]) for resid in range(1, self.ndendr+1)]
            return angle_mask
        return ' '.join([':1' + '@' + atom_name for atom_name in atom_names])

    def all_analysis_available(self):
        print(""" This is the list of the analysis implemented for this class:
                    -   ClassInstance.radius_of_gyration()          ---> compute radius of gyration
                        for each solute molecule;
                    -   ClassInstance.extract_dihedral()            --->
                    -   ClassInstance.extract_CCC_angle()           --->
                    -   ClassInstance.extract_rdf()                 --->
                    -   ClassInstance.extract_ff_distances()        --->
                    -   ClassInstance.extract_c_ho_distances()      --->
                    -   ClassInstance.extract_dend_dend_distances() --->
                    -   ClassInstance.perform_all_analysis()        ---> execute all the analysis above.
                    """)
        print(""" To run all_analysis use the self.all_analysis() method """)

        return

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

    def input_files(self):
        """ return the trajectory and topology files used
            to load the simulation  """
        return (self.filepath+self.filetraj, self.filepath+self.filetop)

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

    ########### DISTANCES #############
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

    def extract_dend_dend_distances(self):
        from compute_DISTANCES import DD_distance
        results = DD_distance(self)
        filename = self._filename('DD_distances')
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

