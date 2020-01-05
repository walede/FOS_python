import statistics as stats
from D import D_Array
import copy
class C_Array(D_Array):
    def __init__(self,N_o, size=10):
        super().__init__(N_o, size=10)
        self.C=[0]*size
        self.C_temp=[0]*size
        self.C_reign=[0]*size
        self.No=N_o

    def C_func(self,y_out,m,pot_can):
        """
        returns the value in the array if in cache, 
        otherwise calculates and returns the value.
        """
        if self.C[m]:
            return self.C[m]
        #if m is not equal to 0
        elif m:
            r_sum=0
            for r in range(m): 
                r_sum += self.alpha_func(pot_can,m,r)*self.C_func(y_out,r,pot_can)
            j=self.No
            result=[]
            for i in y_out[self.No::]:
                result.append(i*pot_can[j])
                j+=1
            self.C[m]=stats.mean(result) - r_sum
            return self.C[m] 
        else:
            self.C[m]=stats.mean(y_out[self.No::])
            return self.C[m]        
            
    def temp_to_def(self):
        """
        Copies the values in the temporary C list to the 
        default list.
        """
        self.C=copy.deepcopy(self.C_temp)
        return None

    def reign_to_temp(self):
        """
        Copies the values in the reigning C list 
        to the temporary list.
        """
        self.C_temp=copy.deepcopy(self.C_reign)
        return None
    
    def def_to_reign(self):
        """
        Copies the values in the default C list 
        to the reigning list.
        """
        self.C_reign=copy.deepcopy(self.C)
        return None
