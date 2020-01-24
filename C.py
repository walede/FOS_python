import numpy as np
from D import D_Array


class C_Array(D_Array):
    def __init__(self, N_o, size=10):
        super().__init__(N_o, size=10)
        self.C = np.zeros((size))
        self.C_temp = np.zeros((size))
        self.C_reign = np.zeros((size))
        self.No = N_o

    def C_func(self,y_out,m,pot_can):
        """
        returns the value in the array if in cache, 
        otherwise calculates and returns the value.
        """
        if self.C[m]:
            return self.C[m]
        #if m is not equal to 0
        elif m:
            r_sum = 0
            for r in range(m): 
                r_sum += self.alpha_func(pot_can,m,r) * self.C_func(y_out,r,pot_can)
            result = np.multiply(pot_can[self.No::], y_out[self.No::])
            self.C[m] = np.mean(result) - r_sum
            return self.C[m] 
        else:
            self.C[m] = np.mean(y_out[self.No::])
            return self.C[m]        
            
    def temp_to_def(self):
        """
        Copies the values in the temporary C list to the 
        default list.
        """
        self.C = np.copy(self.C_temp)
        return None

    def reign_to_temp(self):
        """
        Copies the values in the reigning C list 
        to the temporary list.
        """
        self.C_temp = np.copy(self.C_reign)
        return None
    
    def def_to_reign(self):
        """
        Copies the values in the default C list 
        to the reigning list.
        """
        self.C_reign = np.copy(self.C)
        return None
