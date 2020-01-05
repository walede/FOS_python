from FOS import FOS
import random
import plotly.graph_objects as go
from noise_gen import noise_gen
import mean_square_error as mse

def main():
    x=[random.random() for i in range(3000)]
    x_1000=x[0:1000]
    y=[0.0 for i in range(3000)]
    i=7
    while i<3000:
        #y[i]=-0.78 + 1.25*x[i-2]*x[i-2] - 0.5*y[i-4] + 0.12*x[i-3]*y[i-2] + 0.3*x[i-2]*y[i-3] - 0.3*x[i]*x[i-1]
        y[i]= -0.435 + 0.45*x[i] + 0.5*y[i-1] + 0.35*x[i-1]*y[i-7]+0.099*x[i-2]*x[i] +0.5*y[i-1]*y[i-6]- 0.15*x[i-5]*x[i]
        #y[i] = 0.45 + 0.511*x[i-2]*x[i-2] + 0.6*y[i-3] - 0.8*x[i-3]*x[i-1] + 0.3*x[i-2]*y[i-3] - 0.3*x[i]*x[i-1]
        i+=1    
    z=noise_gen(y,0)    
    z_1000=z[0:1000]
    y_1000=y[0:1000]
    ans_str,ans_num=FOS(x_1000,z_1000,8,8,2)
    err=mse.mse(ans_num,z_1000,7)  
    id_err=mse.ideal_mse(ans_num,z_1000,7)  
    print(ans_str)
    print(f"MSE is {err}")
    print(f"% MSE is {id_err}")
    fig = go.Figure(
    data=[go.Scatter(y=y_1000,name="y[n]"),go.Scatter(y=ans_num,name="Model y[n]"),go.Scatter(y=z_1000,name="Noisy fcn")],
    layout_title_text= "FOS output: " + ans_str
    )
    fig.show()
if __name__ == "__main__": main()
