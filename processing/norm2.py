""" This function is used to compute the row-wise vector norm of X if X is a matrix. If X is a vector (row or column), v is the vector norm.

    :param X
    :type: scalar or vector or matrix 

    :returns: The row-wise vector-norm of matrix X, i.e., the square-root of the sum of the squares for each row. If X is a vector (row or column), v is the vector norm and norm2() is equivalent to the built-in function norm(). But if X is a matrix e.g., a triaxial accelerometer or magnetometer matrix, norm() gives the overall norm of the matrix whereas norm2() gives the vector norm of each row (i.e., the field strength in the case of a magnetometer matrix).
    :rtype: vector

    Example: sampleMatrix = np.array([[0.2, 0.4, -0.7], [-0.3, 1.1, 0.1]])
            norm2(sampleMatrix)
    Returns: [0.83066239 1.14455231]

    Valid: Python
    oko2@calvin.edu
    Last modified: 29 June 2023
    """

import numpy as np

def norm2(X):
    if isinstance(X, list):
        X0 = X
        X = X0['data']
    
    if isinstance(X, np.ndarray):
        sizearray = X.shape
        
        if sizearray[0] == 1 or sizearray[1] == 1:
            v = np.sqrt(np.sum(X**2))
        else:
            v = np.sqrt(np.sum(np.abs(X)**2, axis=1))
    
    elif isinstance(X, np.ndarray) and not isinstance(X, list):
        v = np.sqrt(np.sum(X**2))
    
    return v