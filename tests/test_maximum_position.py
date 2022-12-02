import pyclesperanto_prototype as cle
import numpy as np
from scipy import ndimage

def test_maximum_position_3d():
    np_input= np.asarray([
            [
                [1, 2, 3, 10],
                [4, 16, 6, 11],
                [7, 8, 9, 12]
            ],
            [
                [1, 2, 3, 13],
                [4, 5, 6, 16],
                [7, 8, 9, 15]
            ]
        ])

    reference = ndimage.maximum_position(np_input)
    gpu_input = cle.push(np_input)
    result = cle.maximum_position(gpu_input)

    assert (result == reference)

def test_maximum_position_2d():
    np_input= np.asarray([
                [1, 2, 3, 10],
                [4, 16, 6, 11],
                [7, 8, 9, 12]
        ])

    reference = ndimage.maximum_position(np_input)
    gpu_input = cle.push(np_input)
    result = cle.maximum_position(gpu_input)

    assert (result == reference)
