# Import numpy with an alias
import numpy as np

def test_matrix_subtraction():
    assert (np.array([[1, 2, 3], [3, 2, 1]]) - np.array([[1, 4 , 6], [5, 7, 8]]) == np.array([[0, -2, -3], [-2, -5, -7]])).all()
    assert (np.array([100, 400, 500]) - np.array([400, 322, 454]) == np.array([-300, 78, 46])).all()


def test_shape_array():
    assert (np.array([[12, 54, 65], [12, 54, 54], [63, 43, 32], [1, 3, 5]])).shape == (4, 3)
    assert (np.array([4])).shape == (1,)



    