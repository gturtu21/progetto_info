
def get_trajectory_files():
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

