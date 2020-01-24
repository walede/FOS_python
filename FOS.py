from C import C_Array
from D import D_Array
from g import G_Array
from pick_can import Candidate
from Q import Q_Array
import numpy as np


def FOS(x, y, L, K, order):
    """
    Generates the modeled function based 
    on the inputs and returns the string and numeric format.
    """
    candidates = Candidate(x, L, y, K, order)
    #---generate all the candidates----
    candidates.pick_can()
    stop = False
    labels = {}
    label_str = []
    win_can = None
    num_ans = np.zeros((y.size))
    y_ans = None
    solution_index = 1
    N_o = max(K,L)
    #-- initiate the g,D,C,Q objects----
    g_ans = G_Array()
    D_ans = D_Array(N_o, len(candidates.can_string))
    C_ans = C_Array(N_o, len(candidates.can_string))
    Q_ans = Q_Array(N_o, y, len(candidates.can_string), x.size)
    #--- go through the potential candidates and select the one with the highest Q sore ----
    while len(candidates.can_string) > 1 and stop == False:
        for key, value in candidates.can_string.items():
            curr_can = value
            D_ans.temp_to_def()
            C_ans.temp_to_def()
            for m in range(solution_index+1):
                for r in range(m+1):
                    D_ans.D_func(curr_can,m,r)
                C_ans.D = np.copy(D_ans.D)
                C_ans.C_func(y,m,curr_can)
            g_temp = g_ans.g_func(y,curr_can,m,C_ans,D_ans)
            Q_temp = Q_ans.Q_func(g_temp,solution_index,curr_can,D_ans)
            if Q_temp > Q_ans.Q_reign:
                g_ans.set_g_reign(g_temp)
                Q_ans.set_Q_reign(Q_temp)
                win_can = key
                D_ans.def_to_reign()
                C_ans.D = np.copy(D_ans.D)
                C_ans.def_to_reign()
        #-- check to see if the MSE is reduced, if not we are done looking
        if Q_ans.stop_check(solution_index):
            g_ans.set_g(solution_index)
            D_ans.set_selcan(candidates.can_string[win_can])
            labels[win_can] = candidates.can_string[win_can]
            label_str.append(win_can)
            D_ans.reign_to_temp()
            C_ans.D = np.copy(D_ans.D)
            C_ans.reign_to_temp()
            solution_index += 1
        else: stop = True
        if win_can != None:
            candidates.can_string.pop(win_can)
        else: stop = True
        Q_ans.set_Q_reign(0)
        g_ans.set_g_reign(0)
        win_can = None
    #--put the answers into a string and give the numeric answer as well---
    num_terms = len(labels)
    y_ans = "y[n] = "
    ans_index=0
    for i in range(num_terms+1):
        if i == 0:
            coeff = g_ans.get_coeff(i,num_terms,D_ans.selcan,D_ans)
            rounded = round(coeff,4)
            y_ans += str(rounded) + " + "
            num_ans = np.add(num_ans, coeff)
        elif i == num_terms:
            coeff = g_ans.get_coeff(i,num_terms,D_ans.selcan,D_ans)
            rounded = round(coeff,4)
            y_ans += str(rounded) + "*" + label_str[ans_index] + "."
            interim = np.multiply(coeff, D_ans.selcan[ans_index])
            num_ans = np.add(num_ans, interim)
        else:
            coeff = g_ans.get_coeff(i,num_terms,D_ans.selcan,D_ans)
            rounded = round(coeff,4)
            y_ans += str(rounded) + "*" + label_str[ans_index] + " + "
            interim = np.multiply(coeff, D_ans.selcan[ans_index])
            num_ans = np.add(num_ans, interim)
            ans_index += 1
    return y_ans,num_ans
