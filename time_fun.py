import time

def time_fun(fun):
    start = time.time
    fun()
    end = time.time
    print('Total time:',str(end-start))
    return 
