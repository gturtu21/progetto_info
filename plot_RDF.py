import os 
import sys
import pickle 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from savefig import save_image_SVG

def plot_all_rdf_alltraj():

    """ Produce a plot all rdf for all pickle files present in the current directory """

    pickle_files = [files for files in os.listdir() if os.path.splitext(files)[1]=='.pickle' if 'rdf' in os.path.splitext(files)[0]]
    colors=['r','b','k','m','y','g','c','purple','darkgreen']
    c=0
    for files in pickle_files:
        with open(files,'rb') as pickle_file:
            content = pickle.load(pickle_file)
            couples=list(content.keys())
            for el in couples:
                plt.plot(content[el][0],content[el][1], colors[c],label=files)
            c+=1
    plt.xlim((0.2,10))
    plt.ylim((0,100))
    plt.show()
    return 

def subplot_rdf_etn_vs_tfn():
    def check_cosolvent():
        for el in couples:
            if '_etn_' in el:
                return 0
            if '_tfn_' in el:
                return 1
            if 'WAT' in el:
                return 2
        return 
    """ Produce a horizontal subplot with trajectories in ethanol on the left side,
        trajectories in trifluoroethanol on the right side """
    pickle_files = [files for files in os.listdir() if os.path.splitext(files)[1]=='.pickle' if 'rdf' in os.path.splitext(files)[0]]
    num_files = len(pickle_files)
    ############################## PLOT STYLE ##################################
    fig, axs = plt.subplots(1,2,sharey=False,figsize=(12.5,5.5))
    fig.suptitle('RDF in ETOH (left), RDF in TFE(right)')
    plt.subplots_adjust(wspace=0.0)
    colors1=['blue','darkblue','cornflowerblue','deepskyblue','aquamarine']
    colors2=['red','darkred','salmon','orangered','tomato']
    ############################################################################
    c1=0
    c2=0
    for files in pickle_files:
        with open(files,'rb') as pickle_file:
            content = pickle.load(pickle_file)
            couples=list(content.keys())
        if check_cosolvent()==0:
            for el in couples:
                if el == 'jan_f_jan_f':
                    pass
                else:
                    axs[0].plot(content[el][0], content[el][1], colors1[c1])
            c1+=1
            print('sono c1:'+str(c1))
        elif check_cosolvent()==1:
            for el in couples:
                if el == 'jan_f_jan_f':
                    pass
                else:
                    axs[1].plot(content[el][0],content[el][1], colors2[c2])
            c2+=1
            print('sono c2:'+str(c2))
        else:
            pass
    axs[0].set_xlim((0.2,10))
    axs[0].set_ylim((0,15))
    axs[1].set_xlim((0.2,10))
    axs[1].set_ylim((0,15))
    axs[0].set_ylabel('g(r)')
    axs[0].set_xlabel(r'$r[\AA]$')
    axs[1].set_xlabel(r'$r[\AA]$')
    axs[1].set_yticks([])
    plt.show()
    return

def plot_all_rdf_singletraj():
    """ Produce one plot for each key present in the dictionary """
    #def check_cosolvent():
    #    for el in couples:
    #        if '_etn_' in el:
    #            return 0
    #        if '_tfn_' in el:
    #            return 1
    #        if 'WAT' in el:
    #            return 2
    #    return
    
    ########################
    pickle_files = [files for files in os.listdir() if os.path.splitext(files)[1]=='.pickle' if 'RDF' in os.path.splitext(files)[0]]
    for files in pickle_files:
        #num_dendr=str(1)
        with open(files, 'rb') as pickle_file:
            content = pickle.load(pickle_file)
            couples=list(content.keys())
        #if check_cosolvent()==0:
        #    cosolvent='Ethanol'
        #if check_cosolvent()==1:
        #    cosolvent='Trifluoethanol'
        #if check_cosolvent()==2:
        #    cosolvent='Nocosolvent'
        for el in couples:
            plt.xlim((0.2,10))
            plt.ylim((0,15))
            plt.ylabel('g(r)')
            plt.xlabel(r'$r[\AA]$')
            if 'jan_f_jan_f' in el:
                num_dendr=str(2)
                plt.ylim((0,100))
            plt.plot(content[el][0],content[el][1],'k',label=el) 
            plt.legend()
            #save_image_SVG('Ndendr_'+num_dendr+cosolvent +'_rdf_'+ el)
            save_image_SVG(os.path.splitext(files)[0]+ el)
            plt.clf()

###USAGE

#subplot_rdf_etn_vs_tfn()
plot_all_rdf_singletraj()

