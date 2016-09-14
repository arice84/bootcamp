import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import bootcamp_utils as booU

#parameters
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
dt = 0.01

# Make an array of time points, evenly spaced up to 10
t = np.arange(0, 60, dt)

# Make an array to store the number of bacteria
r = np.empty_like(t)
f = np.empty_like(t)


# Set the initial number of bacteria
r[0] = 10
f[0] = 1


# Write a for loop to keep updating n as time goes on
for i in range(1, len(t)):
    r[i] = r[i-1] + (dt * alpha * r[i-1]) - (dt * beta * f[i-1] * r[i-1])
    f[i] = f[i-1] + (dt * delta * f[i-1] * r[i-1]) - (dt * gamma * f[i-1])

#plot data
plt.plot(t, r, color='black')
plt.plot(t, f, color='red')
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of animals')
plt.legend('rabbits', 'foxes')
plt.title('Modeled Lotka-Volterra model')
plt.show()
