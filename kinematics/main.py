from gettext import translation
import rotate_utils as rotate
import translation_utils as translations
import numpy as np

if __name__ == '__main__':
    theta_1 = 90
    theta_2 = 90
    a1_ = [0, 0, 0]
    a2_ = [3, 0, 0]
    A_1 = rotate.rotate_on_z(theta_1)
    A_2 = translations.translate_p(a1_).dot(rotate.rotate_on_z(theta_2))
    A_3 = translations.translate_p(a2_)
    print(A_3.dot(A_1.dot(A_2)))
