from g import G_Array
from D import D_Array
import numpy as np


class Q_Array(G_Array,D_Array):
    
    def __init__(self, N_o, y_out, size=10, N=1000):
        self.N_o = N_o
        self.Q = np.array([])
        self.Q_reign = 0
        self.N = N
        self.y_out = y_out
        g_0 = np.mean(y_out[self.N_o::])
        self.Q = np.append(self.Q, g_0**2)

    def Q_func(self, g, m, pot_can, D):
        """
        Returns the Q value for the given g.
        """
        return (g**2) * D.D_func(pot_can, m, m)

    def stop_check(self, index):
        """
        Checks to see if the new candidate term improves the 
        result of the program by calculating the Q values.
        """
        left = self.Q_reign
        r_sum = np.sum(self.Q[0:index])
        square = np.power(self.y_out[self.N_o::], 2)
        MSE = np.mean(square) - r_sum
        right = (4 / (self.N - self.N_o+1)) *MSE
        if (left > right) and right > 0:
            if index > 1:
                past_MSE = np.mean(square) -np.sum(self.Q[0:index-1])
                if (MSE / past_MSE) < 0.99:
                    self.set_Q()
                    return True
                else: return False
            self.set_Q()
            return True
        else: return False

    def set_Q(self):
        """
        Adds the Q_reign value to the Q history array.
        """
        self.Q = np.append(self.Q, self.Q_reign)
        return None

    def set_Q_reign(self, value):
        """
        Sets the Q_reign to value, returns None.
        """
        self.Q_reign = value
        return None
