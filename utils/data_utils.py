import numpy as np

def lagged_matrix(m, lags=[0]):
    '''
    Function for creating a time-lagged matrix.

    Inputs:
    - m: a matrix of shape (n_times, n_features)
    - lags: an array-like of indices by which the features of m are displaced

    Outputs:
    - lagged_m: a matrix of shape (n_times, n_features*n_lags), where n_lags is the number of elements in lags
    '''

    lagged_matrices = []
    for lag in lags:
        lagged_matrices.append(
            np.roll(m, lag, axis=0)
        )

    return np.hstack(lagged_matrices)