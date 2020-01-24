import numpy as np


class D_Array:
    def __init__(self, N_o, size=10):
        self.D = np.zeros((size,size))
        self.D[0][0] = 1
        self.D_temp = np.zeros((size,size))
        self.D_reign = np.zeros((size,size))
        self.D_temp[0][0] = 1
        self.No = N_o
        self.selcan = []     
    
    def D_func(self, pot_can, m, r):
        """
        Returns the cached value if already calculated, otherwise
        calculates and returns the value.
        """
        if self.D[m][r]:
            return self.D[m][r]
        elif r == 0:
            self.D[m][r] = np.mean(pot_can[self.No::])
            return self.D[m][r] 
        else:
            r_sum = 0
            for i in range(r):
                r_sum += self.alpha_func(pot_can, r, i)*self.D_func(pot_can, m, i)
            if m == r:
                result = np.power(pot_can[self.No::], 2)
                self.D[m][r] = np.mean(result) - r_sum
                return self.D[m][r]
            else:
                hold = self.selcan[::][r-1]
                result = np.multiply(pot_can[self.No::], np.asarray(hold[self.No::]))
                self.D[m][r] = np.mean(result) - r_sum
                return self.D[m][r]
    
    def alpha_func(self,pot_can,m,r):
        """
        Returns value D[m][r]/D[r][r].
        """
        if self.D[m][r] and self.D[r][r]:
            return self.D[m][r] / self.D[r][r]
        else:
            return self.D_func(pot_can,m,r) / self.D_func(pot_can,r,r)

    def set_selcan(self,win_can):
        """
        Collects the selected candidates, and returns a boolean.
        """
        if any(win_can): #only enter non empty arrays
            self.selcan.append(win_can)
            return True
        else: return False

    def temp_to_def(self):
        """
        Copies the values of the temporary 
        D list to the default list.
        """
        self.D = np.copy(self.D_temp)
        return None
    
    def reign_to_temp(self):
        """
        Copies the values of the reigning 
        D list to the temporary list.
        """        
        self.D_temp = np.copy(self.D_reign)
        return None

    def def_to_reign(self):
        """
        Copies the values of the default
        D list to the reigning list.
        """        
        self.D_reign = np.copy(self.D)
        return None
