import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np


# v = Initial points of vortices [x0,y0,x1,y1...]
# gamma = Strengths for points 0,1,2..
# t = time endpoint
# res = Number of equally spaced time points

v = [1,0, np.cos(2*np.pi/3),np.sin(2*np.pi/3), np.cos(2*np.pi/3),np.sin(-2*np.pi/3)]
gamma = [1, 3, -1]
t = 20
res = 500


def rhs(s, v):
    pairs = [v[i:i+2] for i in range(0, len(v), 2)]
    x = v[::2] 
    y = v[1::2]
    
    # implement ODE for each pair x_alpha, y_alpha
    fn =  [[
        -1/(2*np.pi)*sum(gamma[k]*(y[i]-y[k])/((x[i]-x[k])**2+(y[i]-y[k])**2) for k in range(len(x)) if k!=i), 
        1/(2*np.pi)*sum(gamma[k]*(x[i]-x[k])/((x[i]-x[k])**2+(y[i]-y[k])**2) for k in range(len(x)) if k!=i)
        ] for i in range(len(pairs))]
    return [item for sub in fn for item in sub]


a = solve_ivp(rhs, (0,t), v, t_eval = np.linspace(0,t,res))


#Plot figure of paths

plt.figure()
plt.plot(v[::2], v[1::2], 'o')
for i in range(0, len(v), 2):
    plt.plot(a.y[i], a.y[i+1])
plt.show()