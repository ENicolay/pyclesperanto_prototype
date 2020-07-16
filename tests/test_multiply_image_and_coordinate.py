import pyclesperanto_prototype as cle
import numpy as np


def test_multiply_image_and_coordinate():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4],
        [0, 2, 4, 6, 8]
    ]))

    result = cle.create(test1)
    cle.multiply_image_and_coordinate(test1, result, 0)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)

    assert (np.array_equal(a, b))
    print("ok multiply_image_and_coordinate")
