class AmbMask():
    """ This is a simple class used to write easily Amber masks (Amask)
        thus avoiding to repeat the syntax every time which may
        also lead to typo mistakes"""

    def __init__(self, atom_dict):
        assert type(atom_dict) == dict
        self.resid = atom_dict['resid']
        self.name = atom_dict['name']

    def mask(self):
        return ':' + self.resid + '@' + self.name

class DistMask():
    """ This class will be used to write distance masks  
        whenever a distance has to be computed """

    def __init__(self, atom1, atom2):
        self.dict1 = atom1
        self.dict2 = atom2
        self.atom1 = AmbMask(atom1)
        self.atom2 = AmbMask(atom2)
        if self.atom1.resid < self.atom2.resid:
            self.atoms = [self.atom1.mask(), self.atom2.mask()]
        elif self.atom1.resid > self.atom2.resid:
            self.atoms = [self.atom2.mask(), self.atom1.mask()]
        else:
            if self.atom1.name <= self.atom2.name:
                self.atoms = [self.atom1.mask(), self.atom2.mask()]
            else:
                self.atoms = [self.atom2.mask(), self.atom1.mask()]

    def write(self):
        return ' '.join(self.atoms)

    def __eq__(self, dist2):
        return DistMask(self.dict2, self.dict1).write() == dist2.write()
        
class AngleMask(DistMask, AmbMask):
    """ This class will be used to write angle masks whenever
        an angle has to be computed """

    def __init__(self, atom1, atom2, atom3):
        super().__init__(atom1,atom2)
        self.atom3 = super().__init__(atom3)
        self.atoms.append(self.atom3.mask())


class DihMask(AngleMask):
    """ This class will be used to write angle masks 
        whenever a dihedral angle has to be computed """
    def __init__(self, atom1, atom2, atom3, atom4):
        super().__init__(atom1, atom2, atom3)
        if isistance(atom4, AmbMask):
            self.atoms.append(atom4.mask())

