import numpy as np
import matplotlib.pyplot as plt

# Parameters (change to alter simulation)
v0      = 1.0       # initial velocity
eta     = 0.5       # random angle fluctuations (radians)
L       = 10        # size of box
R       = float(input('Enter interation radius (float less than 5): '))         # interation radius
dt      = 0.2       # time step
Nt      = 200       # numer of time steps 
N       = 1000      # number of simulated particles (birds)
real_time = True

np.random.seed(17)

x = np.random.rand(N, 1)*L
y = np.random.rand(N, 1)*L

theta = 2*np.pi*np.random.rand(N, 1)
v = np.array([v0*np.cos(theta), v0*np.sin(theta)])

fig = plt.figure(figsize=(5, 5), dpi=80)
ax = plt.gca()

for i in range(Nt):
    x += v[0]*dt
    y += v[1]*dt

    x %= L
    y %= L

    mean_theta = theta
    for b in range(N):
        neighbors = (x-x[b])**2+(y-y[b])**2 < R**2
        sx = np.sum(np.cos(theta[neighbors]))
        sy = np.sum(np.sin(theta[neighbors]))
        mean_theta[b] = np.arctan2(sy, sx)

    theta = mean_theta + eta*(np.random.rand(N, 1)-0.5)
    v = np.array([v0*np.cos(theta), v0*np.sin(theta)])

    if real_time: # or (i == Nt-1):
        plt.cla()
        plt.quiver(x, y, *v)
        ax.set(xlim=(0, L), ylim=(0, L))
        ax.set_aspect('equal')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.pause(0.001)

plt.savefig('swarming.png', dpi=240)
plt.show()



