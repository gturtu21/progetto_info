import pickle as pk

def SaveToPickle(data_to_save, filename):
    with open(filename+'.pickle','wb') as currentfile:
        pk.dump(data_to_save,currentfile,protocol=pk.HIGHEST_PROTOCOL)
    return 

