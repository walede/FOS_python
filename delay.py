import numpy as np


def delay(x = np.array([]), delay=0):
    """
    Adds a discrete time delay to the series of values and 
    returns the result in a list.
    """
    array = np.copy(x)
    D = delay if delay<=array.size else array.size
    i = 0
    while i < D:
        array = np.insert(array,0,0.0)
        i += 1
    return array[0:x.size]

#np.insert(arr,2,values)
