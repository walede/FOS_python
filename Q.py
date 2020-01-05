from g import G_Array
from D import D_Array
import statistics as stats

class Q_Array(G_Array,D_Array):
    
    def __init__(self,N_o,y_out,size=10,N=1000):
        self.N_o=N_o
        self.Q=[]
        self.Q_reign=0
        self.N=N
        self.y_out=y_out
        g_0= stats.mean(y_out[self.N_o::])
        self.Q.append(g_0**2)
        #Sets the initial g_0 value through the y_out value

    def Q_func(self,g,m,pot_can,D):
        """
        Returns the Q value for the given g.
        """
        return (g**2)*D.D_func(pot_can,m,m)

    def stop_check(self,index):
        """
        Checks to see if the new candidate term improves the 
        result of the program by calculating the Q values.
        """
        left=self.Q_reign
        r_sum= sum(self.Q[0:index])
        square=[x**2 for x in self.y_out[self.N_o::]]
        MSE=stats.mean(square) - r_sum
        right=(4/(self.N-self.N_o+1))*MSE
        if (left>right) and right>0:
            if index>1:
                past_MSE= stats.mean(square) -sum(self.Q[0:index-1])
                if(MSE/past_MSE)<0.99:
                    self.set_Q()
                    #if (stats.mean(square) -sum(self.Q)<=0): #messed up here
                        #return False
                    return True
                else: return False
            self.set_Q()
            #if (stats.mean(square) -sum(self.Q)<=0):
                #return False
            return True
        else: return False

    def set_Q(self):
        """
        Adds the Q_reign value to the Q history array.
        """
        self.Q.append(self.Q_reign)
        return None

    def set_Q_reign(self,value):
        """
        Sets the Q_reign to value, returns None.
        """
        self.Q_reign=value
        return None