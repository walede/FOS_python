import numpy as np 


def noise_gen(y_in, percentage=0):
    v = percentage * np.var(y_in) / 100
    noise = np.random.normal(0, v**0.5, y_in.size)
    z = np.add(noise, y_in)
    return z
