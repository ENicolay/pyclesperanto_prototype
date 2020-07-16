import pyclesperanto_prototype as cle
import numpy as np


def test_transpose_xy():
    test1 = cle.push(np.asarray([
        [
            [0, 1],
            [2, 3]
        ], [
            [4, 5],
            [6, 7]
        ]
    ]))

    reference = cle.push(np.asarray([
        [
            [0, 1],
            [4, 5]
        ], [
            [2, 3],
            [6, 7]
        ]
    ]))

    result = cle.create(test1)
    cle.transpose_xy(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert (np.array_equal(a, b))
    print("ok transpose_xy")