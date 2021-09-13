class AmbMask():
    """ This is a simple class used to write easily Amber masks (Amask)
        thus avoiding to repeat the syntax every time which may
        also lead to typo mistakes"""

    def __init__(self, atom_dict):
        self.resid = atom_dict['resid']
        self.name = atom_dict['name']

    def mask(self):
        return ':' + self.resid + '@' + self.name

class DistMask():
    """ This class will be used to write distance masks  
        whenever a distance has to be computed """
    def __init__(self, atom1, atom2):
        if isinstance(atom1,AmbMask) and isinstance(atom2,AmbMask):    
            self.atoms = [atom1.mask(), atom2.mask()]
    def write(self):
        return ' '.join(self.atoms)
        
class AngleMask(DistMask):
    """ This class will be used to write angle masks whenever
        an angle has to be computed """
    def __init__(self, atom1, atom2, atom3):
        super().__init__(atom1,atom2)
        if isinstance(atom3,AmbMask):
            self.atoms.append(atom3.mask())


class DihMask(AngleMask):
    """ This class will be used to write angle masks 
        whenever a dihedral angle has to be computed """
    def __init__(self, atom1, atom2, atom3, atom4):
        super().__init__(atom1, atom2, atom3)
        if isistance(atom4, AmbMask):
            self.atoms.append(atom4.mask())

