def delay(x=[],delay=0):
    """
    Adds a discrete time delay to the series of values and 
    returns the result in a list.
    """
    array=list(x)
    D=delay if delay<=len(array) else len(array)
    i=0
    while i < D:
        array.pop()
        array.insert(0,0.0)
        i+=1
    return array

