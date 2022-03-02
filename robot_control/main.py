## PID control

# Import dependencies
import numpy as np
import scipy as sp
import control
import matplotlib.pyplot as plt
from math import pow, pi

if __name__ == '__main__':
    # Robot parameters
    m = 1 # Robot mass
    l = 1 # Robot length
    lc = 0.5 # Distance to center of mass
    B = 0.01 # Friction coefficient
    I = (1/3) * m * pow(l, 2) # Inertia
    g = 9.81 # Gravity acceleration

    # Gain
    K = pi/4

    # PID parameters
    Kp = 8
    Ti = 0.3
    Td = 0.5

    # Simulation time interval
    start = 0
    stop = 5
    step = 0.01

    time = np.arange(start, stop, step)

    # Transfer function parameters
    alfa_1 = B * pow(lc, 2)/ (m * pow(lc, 2) + I)
    alfa_0 = m * g * lc
    gama = 1/(m*pow(lc,2)+I)
    b2 = gama*Kp*Ti*Td
    b1 = gama*Kp*Ti
    b0 = gama*Kp; a3 = Ti
    a2 = Ti*alfa_1+gama*Kp*Ti*Td
    a1 = Ti*alfa_0+gama*Kp*Ti
    a0 = gama*Kp

    num = np.array([K*b2, K*b1, K*b0])
    den = np.array([a3, a2, a1, a0])

    H = control.tf(num, den)
    print(f"T(s) = {H}")

    t, y = control.step_response(H, time)
    plt.plot(t, y)
    plt.title("PID control")
    plt.xlabel("t")
    plt.ylabel("Robot angle")
    plt.grid()
    plt.savefig('plots/transfer_function.png')

