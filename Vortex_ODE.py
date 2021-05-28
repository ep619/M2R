import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

v = [-1,-2, 1,2, -1,2]
#-> [[0,0],[1,1]]
gamma = [1,1,1]

def rhs(s, v):
    pairs = [v[i:i+2] for i in range(0, len(v), 2)]
    x = v[::2]
    y = v[1::2]
    #return [[1/(2*np.pi)*sum(gamma[k]*(y[i]-y[k])/((x[i]-x[k])**2+(y[i]-y[k])**2) for k in range(len(x)) if k!=i), 1/(2*np.pi)*sum(gamma[k]*(x[j]-x[k])/((x[j]-x[k])**2+(y[j]-y[k])**2) for k in range(len(x)) if k!=j)] for i,j in pairs]
    fn =  [[1/(2*np.pi)*sum(gamma[k]*(y[i]-y[k])/((x[i]-x[k])**2+(y[i]-y[k])**2) for k in range(len(x)) if k!=i), 1/(2*np.pi)*sum(gamma[k]*(x[i]-x[k])/((x[i]-x[k])**2+(y[i]-y[k])**2) for k in range(len(x)) if k!=i)] for i in range(len(pairs))]
    return [item for sub in fn for item in sub]

a = solve_ivp(rhs, (0,10), v, t_eval = np.linspace(0,10,1000))

plt.figure()
for i in range(0, len(v), 2):
    plt.plot(a.y[i], a.y[i+1])
plt.show()