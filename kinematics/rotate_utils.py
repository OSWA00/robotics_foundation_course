from math import sin, cos, radians
import numpy as np

def rotate_on_x(alpha):
    alpha = radians(alpha)
    return np.array([
        [1, 0, 0, 0],
        [0, cos(alpha), -sin(alpha), 0],
        [0, sin(alpha), cos(alpha), 0],
        [0, 0, 0, 1]
    ])

def rotate_on_y(phi):
    phi = radians(phi)
    return np.array([
        [cos(phi), 0, sin(phi), 0],
        [0, 1, 0, 0],
        [-sin(phi), 0, cos(phi), 0],
        [0, 0, 0, 1]
    ])

def rotate_on_z(theta):
    theta = radians(theta)
    return np.array([
        [cos(theta), -sin(theta), 0, 0],
        [sin(theta), cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def homogenous_rotation(r, d, theta, alpha):
    theta = radians(theta)
    alpha = radians(alpha)
    return np.array([
        [cos(theta), -sin(theta) * cos(alpha), sin(theta) * sin(alpha), r * cos(theta)],
        [sin(theta), cos(theta)* cos(alpha), -cos(theta) * sin(alpha), r * sin(theta)],
        [0, sin(alpha), cos(alpha), d],
        [0, 0, 0, 1]
    ])