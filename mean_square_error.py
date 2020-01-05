import statistics as stats

def mse(model,y_in,N_o):
    result= [x1-x2 for x1,x2 in zip(y_in[N_o::],model[N_o::])]
    result2= [x**2 for x in result]
    return stats.mean(result2)

def ideal_mse(model,y_in,N_o):
   result= [x1-x2 for x1,x2 in zip(model[N_o::],y_in[N_o::])]
   result2= [x**2 for x in result]
   result3=stats.mean(result2)
   result4= result3/stats.variance(y_in)
   return 100*result4
