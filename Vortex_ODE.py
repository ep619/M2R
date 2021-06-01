import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np


# v = Initial points of vortices [x0,y0,x1,y1...]
# gamma = Strengths for points 0,1,2..
# t = time endpoint
# res = Number of equally spaced time points

v = [1,0, np.cos(2*np.pi/3),np.sin(np.pi/3), 4*np.cos(np.pi/5), -np.sin(2*np.pi/3)]
gamma = [8,8,8]
t = 20
res = 10000
tarr = np.linspace(0,t,res)


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


a = solve_ivp(rhs, (0,t), v, t_eval=tarr)


#Plot figure of paths

plt.figure()
plt.plot(v[::2], v[1::2], 'o')


for i in  range(0, len(v), 2):
    plt.scatter(a.y[i], a.y[i+1], linewidth=0.2, c=tarr , cmap=plt.cm.viridis , marker=".", s=4)
plt.colorbar(plt.scatter(a.y[0], a.y[1], linewidth=0.2, c=tarr ,cmap=plt.cm.viridis , marker=".",s=4), shrink=0.8, label='t')

plt.axis('equal')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

