def savetoSVG(fname):
    import matplotlib.pyplot as plt
    fname=fname+'.svg'
    plt.savefig(fname,format='svg')
    return 
