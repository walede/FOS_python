import numpy as np


def mse(model,y_in,N_o):
    diff = np.subtract(y_in[N_o::], model[N_o::])
    square = np.power(diff, 2)
    mean = np.mean(square)
    return mean

def percent_mse(model,y_in,N_o):
   diff = np.subtract(model[N_o::],y_in[N_o::])
   square = np.power(diff, 2)
   mean = np.mean(square)
   percent = mean / np.var(y_in)
   return 100 * percent
