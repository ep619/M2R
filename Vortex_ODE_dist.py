import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np


# v = Initial points of vortices [x0,y0,x1,y1...]
# gamma = Strengths for points 0,1,2..
# t = time endpoint
# res = Number of equally spaced time points

v = np.array([1.4,0, -0.5,0.8, -1.25,-2.1])
gamma = [12, 5, 6]
t = 30
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

for i in  range(0, 1, 2):
    plt.scatter(a.y[i], a.y[i+1], linewidth=0.4, c=tarr , cmap=plt.cm.viridis , marker=".", s=6)
plt.colorbar(plt.scatter(a.y[0], a.y[1], linewidth=0.4, c=tarr ,cmap=plt.cm.viridis , marker=".",s=6), shrink=0.8, label='t')

plt.axis('equal')
plt.xlabel("x")
plt.ylabel("y")

# init_conditions from gaussian_dist
for i in range(6):
    init_dist = np.random.default_rng().normal(0,0.05,6)
    init_dist[2:] = 0
    v1 = v+init_dist
    b = solve_ivp(rhs, (0,t), v1, t_eval=tarr)
    for i in range(0,1, 2):
        plt.plot(b.y[i], b.y[i+1], linewidth=0.6)
plt.show()