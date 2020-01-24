from delay import delay
import numpy as np
class Candidate():

    def __init__(self,x,L,y,K,order=2):
        self.x = x
        self.y = y
        self.L = L
        self.K = K
        self.order = order
        self.can_string = {}
            
    def pick_can(self):
        if self.order not in [1, 2, 3]:
            self.order = 2
        
        for l in range(self.L+1):
            self.can_string[f'x[n-{l}]'] = delay(self.x, l)
        for k in range(1,self.K+1):
            self.can_string[f'y[n-{k}]'] = delay(self.y, k)

        if self.order > 1:
            for l_1 in range(self.L+1):
                for l_2 in range(l_1, self.L+1):
                    self.can_string[f'x[n-{l_1}]*x[n-{l_2}]'] = np.multiply(delay(self.x, l_1), delay(self.x, l_2))
            for k_1 in range(1,self.K+1):
                for k_2 in range(k_1,self.K+1):
                    self.can_string[f'y[n-{k_1}]*y[n-{k_2}]'] = np.multiply(delay(self.y, k_1), delay(self.y, k_2))
            for k in range(1,self.K+1):
                for l in range(self.L+1):
                    self.can_string[f'x[n-{l}]*y[n-{k}]'] = np.multiply(delay(self.x, l), delay(self.y, k))

        if self.order > 2:
            for l_1 in range(self.L+1):
                for l_2 in range(l_1, self.L+1):
                    for l_3 in range (l_2, self.L+1):
                        self.can_string[f'x[n-{l_1}]*x[n-{l_2}]*x[n-{l_3}]'] = delay(self.x, l_1) * delay(self.x, l_2) * delay(self.x, l_3)
            for k_1 in range(1, self.K+1):
                for k_2 in range(k_1, self.K+1):
                    for k_3 in range (k_2, self.K+1):
                        self.can_string[f'y[n-{k_1}]*y[n-{k_2}]*y[n-{k_3}]'] = delay(self.y, k_1) * delay(self.y, k_2) * delay(self.y, k_3)
            for l_1 in range(self.L+1):
                for l_2 in range(l_1, self.L+1):
                    for k in range (1, self.K+1):
                        self.can_string[f'x[n-{l_1}]*x[n-{l_2}]*y[n-{k}]'] = delay(self.x, l_1) * delay(self.x, l_2) * delay(self.y, k)
            for k_1 in range(1, self.K+1):
                for k_2 in range(k_1, self.K+1):
                    for l in range (self.L+1):
                        self.can_string[f'x[n-{l}]*y[n-{k_1}]*y[n-{k_2}]'] = delay(self.y, k_1) * delay(self.y, k_2) * delay(self.x, l)
