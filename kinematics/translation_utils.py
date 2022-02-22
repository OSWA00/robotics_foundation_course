from math import sin, cos
import numpy as np

def translate_p(p_vector):
    return np.array([
        [1, 0, 0, p_vector[0]],
        [0, 1, 0, p_vector[1]],
        [0, 0, 1, p_vector[2]],
        [0, 0, 0, 1]
    ])

