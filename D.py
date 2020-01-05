import statistics as stats
import copy
class D_Array:
    def __init__(self, N_o, size=10):
        self.D=[[0]*size for i in range(size)]
        self.D[0][0]=1
        self.D_temp=[[0]*size for i in range(size)]
        self.D_reign=[[0]*size for i in range(size)]
        self.D_temp[0][0]=1
        self.No=N_o
        self.selcan=[]      
    
    def D_func(self,pot_can,m,r):
        """
        Returns the cached value if already calculated, otherwise
        calculates and returns the value.
        """
        if self.D[m][r]:
            return self.D[m][r]
        elif r==0:
            self.D[m][r]= stats.mean(pot_can[self.No::])
            return self.D[m][r] 
        else:
            r_sum=0
            for i in range(r):
                r_sum += self.alpha_func(pot_can,r,i)*self.D_func(pot_can,m,i)
            if m==r:
                result=[x*x for x in pot_can[self.No::]]
                self.D[m][r]=stats.mean(result) - r_sum #stats.mean(result[::]) - r_sum
                return self.D[m][r]
            else:
                hold=self.selcan[::][r-1]
                j=self.No
                result=[]
                for i in pot_can[self.No::]:
                    result.append(i*hold[j])
                    j+=1
                self.D[m][r]=stats.mean(result) - r_sum
                return self.D[m][r]
    
    def alpha_func(self,pot_can,m,r):
        """
        Returns value D[m][r]/D[r][r].
        """
        if self.D[m][r] and self.D[r][r]:
            return self.D[m][r]/self.D[r][r]
        else:
            return self.D_func(pot_can,m,r)/self.D_func(pot_can,r,r)

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
        self.D=copy.deepcopy(self.D_temp)
        return None
    
    def reign_to_temp(self):
        """
        Copies the values of the reigning 
        D list to the temporary list.
        """        
        self.D_temp=copy.deepcopy(self.D_reign)
        return None

    def def_to_reign(self):
        """
        Copies the values of the default
        D list to the reigning list.
        """        
        self.D_reign=copy.deepcopy(self.D)
        return None