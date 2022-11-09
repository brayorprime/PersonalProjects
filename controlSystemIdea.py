# C Morse, 2022
# A challenge to myself to create a PID control system for a spinning wheel 2D 
# wheel. idk should be fun
from matplotlib import pyplot as plt
import numpy as np

# Inital values
Radinit = 2 # Rad/s
radius = 1  # m
mass = 1    # kg

# PID Settings
P = 0.5
I = 0.5
D = 0.5


# Desired Velocity
RadF = 5    # Rad/s

# Line to show desired and init conditions
RadinitL = np.zeros(2000) + Radinit
RadFL = np.zeros(2000) + RadF

rng = np.random.default_rng(12345)
y = rng.random(size = 2000) 
t = range(0,2000)

Rad = np.empty(2000)
Rad[0] = Radinit

for i in t:
    if Rad[i] > RadF:
        print()







fig = plt.figure()
plt.scatter(t, y)
plt.plot(t, RadinitL, color = 'red')
plt.plot(t, RadFL, color = 'yellow')
plt.grid()



