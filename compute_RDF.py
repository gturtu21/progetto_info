import os
import pytraj as pt
import numpy as np

os.environ["OPENBLAS_NUM_THREADS"] = "1"


########  ETHANOL:  #########   ##### TRIFLUOROETHANOL: ##  
####### ATOM TYPES ##########   #####   atom types  ######
#      1 C    c3    ETN     #   #     1 C    c3    TFN   #
#      2 C1   c3    ETN     #   #     2 C1   c3    TFN   #
#      3 H    hc    ETN     #   #     3 H    h1    TFN   #
#      4 H1   hc    ETN     #   #     4 H1   h1    TFN   #
#      5 H2   hc    ETN     #   #     5 O    oh    TFN   #
#      6 H3   h1    ETN     #   #     6 H2   ho    TFN   #
#      7 H4   h1    ETN     #   #     7 F    f     TFN   #
#      8 O    oh    ETN     #   #     8 F1   f     TFN   #
#      9 H5   ho    ETN     #   #     9 F2   f     TFN   #
#############################   ##########################



def all_rdf(mytraj):
    def rdf(mysolventmask, mysolutemask):
        """ compute the Radial Distribution Function between two groups of atoms
            given in mysolventmask and mysolutemask.
            The output is a python array object """
        return pt.rdf(mytraj,solvent_mask=mysolventmask,bin_spacing=0.1, maximum=10.0, solute_mask=mysolutemask, intramol=False)
    data={}
   ################## COMPUTE RDF BETWEEN DENDRONS ##################
    if mytraj.ndendr > 1:
        rdf_couples=[(':JAN@%f',':JAN@%f','jan_f_jan_f'),(':JAN@%o',':JAN@%ho','jan_ox_jan_ho'),(':JAN@%oh',':JAN@%oh','jan_oh_jan_oh')]
        for couples in rdf_couples:
            couple_name=str(couples[2])
            data[couple_name]=rdf(couples[0],couples[1])
            print('Done with couple:'+couple_name)
    ################# COMPUTE RDF BETWEEN DENDRONS AND ETHANOL #################################
    if mytraj.cosolvent=='ETN':
        rdf_couples=[(':JAN@%o',':ETN@%ho','jan_ox_etn_ho'),(':JAN@%f',':ETN@%hc','jan_f_etn_ch3'),(':JAN@%f',':ETN@%ho','jan_f_etn_ho'),(':JAN@%nc',':ETN@%hc','jan_triazole_etn_ch3'),(':JAN@%c3',':ETN@%hc','jan_csp3_etn_ch3'),(':JAN@%cc',':ETN@%hc','jan_csp2triaz_etn_ch3'),(':JAN@%c',':ETN@%hc','jan_ccarbonyl_etn_ch3'),(':ETN@%hc',':ETN@%hc','etn_ch3_etn_ch3'),(':JAN@%hc',':ETN@%hc','jan_hc_etn_ch3'),(':JAN@%oh',':ETN@%oh','jan_oh_etn_oh')]
        for couples in rdf_couples:
            couple_name = couples[2]
            data[couple_name] = rdf(couples[0],couples[1])
        return data
    ################# COMPUTE RDF BETWEEN DENDRONS AND TRIFLUOROETHANOL #################################
    if mytraj.cosolvent=='TFN': 
        rdf_couples=[(':JAN@%o',':TFN@%ho','jan_ox_tfn_ho'),(':JAN@%f',':TFN@%f','jan_f_tfn_cf3'),(':JAN@%f',':TFN@%ho','jan_f_tfn_ho'),(':JAN@%nc',':TFN@%f','jan_triazole_tfn_cf3'),(':JAN@%c3',':TFN@%f','jan_csp3_tfn_cf3'),(':JAN@%cc',':TFN@%f','jan_csp2triaz_tfn_cf3'),(':JAN@%c',':TFN@%f','jan_ccarbonyl_tfn_cf3'),(':TFN@%f',':TFN@%f','tfn_cf3_tfn_cf3'),(':JAN@%hc',':TFN@%f','jan_hc_tfn_cf3'),(':JAN@%oh',':TFN@%oh','jan_oh_tfn_oh')]
        for couples in rdf_couples:
            couple_name = couples[2]
            data[couple_name] = rdf(couples[0],couples[1])
        return data
    ################# COMPUTE RDF BETWEEN DENDRONS AND WATER #################################
    else:
        rdf_couples=[(':JAN@%o',':WAT@%HW','jan_ox_wat_hw'),(':JAN@%ho',':WAT@%OW','jan_ho_wat_ow')]
        for couples in rdf_couples:     
            couple_name = couples[2]
            data[couple_name] = rdf(couples[0],couples[1])
        return data 



