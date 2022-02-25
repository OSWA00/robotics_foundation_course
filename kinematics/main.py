import rotate_utils as rotate
import translation_utils as translations
import numpy as np

if __name__ == '__main__':
    d1 = 1
    d2 = 1
    d3 = 1
    theta1 = 30
    theta2 = 30
    theta3 = 30
    print(rotate.homogenous_rotation(0, d1, theta1, 0))
    print("------------------------------------------")
    print(rotate.homogenous_rotation(0, d2, theta2, -90))
    print("------------------------------------------")
    print(rotate.homogenous_rotation(0, d3, theta3, 0))
    print("------------------------------------------")
