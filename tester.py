from FOS import FOS
from noise_gen import noise_gen
import mean_square_error as mse
import numpy as np
import timeit
import matplotlib.pyplot as plt
import mplotlib_toggle as plt_toggle


def main():
    x = np.random.rand(3000)
    x_1000 = x[0:1000]
    y = np.zeros((3000))
    i = 3
    _max = i
    while i < 3000:
        #y[i] = -0.78 + 1.25*x[i-2]*x[i-2]*y[i-1] - 0.5*y[i-4]\
                #+ 0.12*x[i-3]*x[i-2]*x[i-3] + 0.3*x[i-2]*x[i-3]*x[i-2]\
                #- 0.3*x[i]*x[i-1]

        #y[i] = -0.435 + 0.45*x[i] + 0.5*y[i-1] + 0.35*x[i-1]*y[i-7]\
                #+ 0.099*x[i-2]*x[i] + 0.5*y[i-1]*y[i-6] - 0.15*x[i-5]*x[i]

        y[i] = 0.45 + 0.511*x[i-2]*x[i-2] + 0.6*y[i-3] - 0.8*x[i-3]*x[i-1]\
               + 0.3*x[i-2]*y[i-3] - 0.3*x[i]*x[i-1]

        i += 1  
    #Generate noise on the function -------------------- 
    z = noise_gen(y, 0)    
    z_1000 = z[0:1000]
    y_1000 = y[0:1000]
    #Run the FOS function --------------------------
    ans_str,ans_num=FOS(x_1000,z_1000,10,10,2)
    #Calculate the error ---------------------------------
    err=mse.mse(ans_num,z_1000,_max)  
    id_err=mse.percent_mse(ans_num,z_1000,_max)  
    #Print solution and error metrics ----------------------
    print(ans_str)
    print(f"MSE is {err}")
    print(f"% MSE is {id_err}")
    #configure the figure -------------------------------
    fig, ax = plt.subplots()
    ax.plot(y_1000, 'r-', label='y[n]', linewidth=1.4)
    ax.plot(ans_num, 'b-', label='Model y[n]', linewidth=1.4)
    ax.plot(z_1000, 'g--', label='Noisy y[n]', linewidth=1.4)
    fig.suptitle(f'FOS Output')
    ax.legend()
    leg = plt_toggle.interactive_legend(ax)
    # plot the figure -------------------------------------
    plt.show()

    
if __name__ == "__main__": 
    main()
