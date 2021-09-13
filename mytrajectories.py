
def trajectory_files():
    """ The function returns the list containing all the path to possible trajectories : 
    - 0: Two fdg3 in etoh 5%; 
    - 1: One fdg3 in etoh 5% ; 
    - 2: One fdg3 in water; 
    - 3: Two fdg3 in fetoh (0-100 ns) ; 
    - 4: Two fdg3 in fetoh (100-200 ns) ; 
    - 5: Two fdg3 in fetoh (0-200 ns);  
    - 6: Two fdg3 in etoh (0-200 ns); 
    - 7: One fdg3 in tfetoh 5%;
    - 8: One fdg3 in etoh 25%;
    - 9: Two fdg3 in etoh 25%.
    """
    common = '/home/giorgio/dpd_metrangolo/gaff_charges/fdg3/'
    mytrajectories_list = [(common+'box_water_ethanol_5pc_100/production_merged/','wrapped_din.nc','dimer_wtet5pc.prmtop'), \
        (common+'FD3_IN_WATER_ETHANOL_5PC/','din.nc','fdg3_wtet5pc.prmtop'), \
        (common+'box_just_water/production/','din.nc', 'fdg3_wt.prmtop'), \
        (common+'box_water_tfethanol_5pc_100_close_dendrons/production/', 'din.nc', 'dimer_wtfet5pc.prmtop'), \
        (common+'box_water_tfethanol_5pc_100_close_dendrons/production/', 'wrapped_din_rst.nc', 'dimer_wtfet5pc.prmtop'), \
        (common+'box_water_tfethanol_5pc_100_close_dendrons/production/','dintot.nc', 'dimer_wtfet5pc.prmtop'), \
        (common+'box_water_ethanol_5pc_100/production_tainah/','din.nc', 'dimer_wtet5pc.prmtop'), \
        (common+'FD3_IN_WATER_TFETHANOL_5PC/','din.nc','fdg3_wtfet5pc.prmtop'), \
        (common+'FD3_IN_WATER_ETHANOL_25PC/','din.nc','fdg3_wtet25pc.prmtop'), \
        (common+'box_water_ethanol_25pc_100_close_dendrons/production/','wrapped_din.nc','dimer_wtet25pc.prmtop')]
    return mytrajectories_list


def trajectory_description():
    traj_descr = ['Two FDG3 molecules in ETN 5%', \
                  'One FDG3 molecule in ETN 5%', \
                  'One FDG3 molecule in pure WATER', \
                  'Two FDG3 molecules in TFN 5% (0-100ns)', \
                  'Two FDG3 molecules in TFN 5% (100-200ns)', \
                  'Two FDG3 molecules in TFN 5% (0-200ns)', \
                  'Two FDG3 molecules in ETN 5% (0-200ns)', \
                  'One FDG3 molecule in TFN 5%', \
                  'One FDG3 molecule in ETN 25%', \
                  'Two FDG3 molecules in ETN 25%']
    return traj_descr

def my_traj_class_usage():
    traj_usage = ["instantiate as my_traj(0, 'ETN', 2, 5, 0, 1000)",\
                  "instantiate as my_traj(1, 'ETN', 1, 5, 0, 1000)",\
                  "instantiate as my_traj(2,  None, 1, 0, 0, 1000)",\
                  "instantiate as my_traj(3, 'TFN', 2, 5, 0, 1000)",\
                  "instantiate as my_traj(4, 'TFN', 2, 5, 0, 1000)",\
                  "instantiate as my_traj(5, 'TFN', 2, 5, 0, 2000)",\
                  "instantiate as my_traj(6, 'ETN', 2, 5, 0, 2000)",\
                  "instantiate as my_traj(7, 'TFN', 1, 5, 0, 1000)",\
                  "instantiate as my_traj(8, 'ETN', 1, 25, 0, 1000)",\
                  "instantiate as my_traj(9, 'ETN', 2, 25, 0, 1000)"]
    return traj_usage                                         
                                                              


