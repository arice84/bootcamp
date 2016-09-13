import numpy as np

def xa_to_dia(xa):
    '''
    Convert an array of cross-sectional areas to diameters wih units
    '''

    diameter = np.sqrt(xa *4 / np.pi)
