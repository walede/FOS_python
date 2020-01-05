import numpy as np 
import statistics as stats 

def noise_gen(y_in, percentage=0):
    v=percentage*stats.variance(y_in)/100
    noise=np.random.normal(0,v**0.5,len(y_in))
    noise_list=list(noise)
    z=[x1+x2 for x1,x2 in zip(noise_list,y_in)]
    return z