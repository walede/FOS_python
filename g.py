from C import C_Array
from D import D_Array
import numpy as np


class G_Array(C_Array,D_Array):
    def __init__(self):
        self.g=np.array([])
        self.g_reign=0
        self.first=True

    def g_func(self,yo,pot_can,m,C,D):
        """
        Returns the value of g for C and D array.
        """
        if self.first:
            self.g = np.append(self.g,(C.C_func(yo,0,pot_can)/D.D_func(pot_can,0,0)))
            self.first=False
        #np.seterr('raise')
        return C.C_func(yo,m,pot_can)/D.D_func(pot_can,m,m)

    def set_g(self,index):
        """
        Sets the value of g in the array and returns the value.
        """
        self.g = np.append(self.g, self.g_reign) 
        return None

    def get_coeff(self,m,terms,sel_can,D):
        """
        Returns the coefficient constant through a recursive g and v 
        calculation.
        """
        r_sum=0
        for i in range(m,terms+1):
            r_sum += self.g[i]*self.get_v(i,m,sel_can,D)
        return r_sum
    
    def get_v(self,i,m,sel_can,D):
        """
        Calculates v through a recursive call multiplied 
        by the alpha function calculation.
        """
        r_sum=0
        if i==m: 
            return 1
        else:
            for r in range(m,i): #or is it m+1
                r_sum -= D.alpha_func(sel_can[i-1],i,r)*self.get_v(r,m,sel_can,D)
            return r_sum

    def set_g_reign(self,value):
        """
        Sets self.g_reign to value.
        """
        self.g_reign=value
        return None
