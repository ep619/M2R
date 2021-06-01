import numpy as np
import matplotlib.pyplot as plt
ICs = np.array([-0.587,-0.563,16.870])
dt = 0.001
a=1/np.sqrt(dt)
print(a)
def g1(tn):
    g1s = [a*(pow(2,-1/2) - 0.5)]
    for i in range(1,int(tn/dt)+1):
        if g1s[i-1]<0:
            g1s.append(2*g1s[i-1]+a/2)
        else:
            g1s.append(-2*g1s[i-1]+a/2)
    return g1s

    
def g2(tn):
    g2s = [a*(pow(3,-1/2) - 0.5)]
    for i in range(1,int(tn/dt)+1):
        if g2s[i-1]<0:
            g2s.append(2*g2s[i-1]+a/2)
        else:
            g2s.append(-2*g2s[i-1]+a/2)
    return g2s
def g3(tn):
    g3s = [a*(pow(5,-1/2) - 0.5)]
    for i in range(1,int(tn/dt)+1):
        if g3s[i-1]<0:
            g3s.append(2*g3s[i-1]+a/2)
        else:
            g3s.append(-2*g3s[i-1]+a/2)
    return g3s

def g(tn):
    return np.array([g1(tn),g2(tn),g3(tn)])

def f(z):
    return np.array([10*(z[1]-z[0]),z[0]*(28-z[2])-z[1], z[0]*z[1]-8/3*z[2]])

def z(tn):
    newz = ICs
    points = []
    gs=g(tn)
    for i in range(int(tn/dt)+1):
        oldz = newz
        points.append(oldz)
        newz = points[i]+dt*(f(points[i])+np.array([gs[0][i],gs[1][i],gs[2][i]]))
    return points

def zref(tn):
    xpoints = []
    ypoints = []
    zpoints = []
    zs = z(tn)
    for i in range(int(tn/dt)+1):
        xpoints.append(zs[i][0])
        ypoints.append(zs[i][1])
        zpoints.append(zs[i][2])
    return [xpoints, ypoints,zpoints]

from mpl_toolkits import mplot3d
plt.figure()
plt.axes(projection='3d')
plt.plot(zref(10)[0],zref(10)[1],zref(10)[2])
plt.show()