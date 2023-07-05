""" This function is used to compute the norm-jerk from triaxial acceleration data.

    :param A: A tag sensor data list or a nx3 acceleration matrix with columns [ax ay az]. Acceleration can be in any consistent unit, e.g., g or m/s^2. A can be in any frame as the norm-jerk is rotation independent. A must have at least 2 rows (i.e., n>=2).
    :type: list or matrix

    :returns: The norm-jerk from triaxial acceleration data in the form of a column vector with the same number of rows as in A, or a tag sensor data structure (if the input A was one). The norm-jerk is ||dA/dt||, where ||x|| is the 2-norm of x, i.e., the square-root of the sum of the squares of each axis. If the unit of A is m/s^2, the norm-jerk has unit m/s^3. If the unit of A is g, the norm-jerk has unit g/s. As j is the norm of the jerk, it is always positive or zero (if the acceleration is constant). The final value in j is always 0 because the last finite difference cannot be calculated.
    :rtype: vector

    Example: sampleMatrix = np.array([[1, 2, 3], [2, 2, 4], [1, -2, 4], [4, 4, 4]])
        njerk(sampleMatrix, 5)
    Returns: [ 7.07106781 20.61552813 33.54101966  0.        ]

    Valid: Python
    oko2@calvin.edu
    Last modified: 29 June 2023
    """

import numpy as np
from datetime import datetime

def njerk(A, sampling_rate):
    if isinstance(A, dict):
        sampling_rate = A["sampling_rate"]
        a = A["data"]
        j = A.copy()
        j["data"] = np.concatenate((sampling_rate * np.sqrt(np.sum(np.diff(a, axis=0)**2, axis=1)), [0]))
        j["creation_date"] = datetime.now().isoformat()
        j["type"] = "njerk"
        j["full_name"] = "norm jerk"
        j["description"] = j["full_name"]
        j["unit"] = "m/s3"
        j["unit_name"] = "meters per seconds cubed"
        j["unit_label"] = "m/s^3"
        j["column_name"] = "jerk"
    else:
        a = A
        j = sampling_rate * np.concatenate((np.sqrt(np.sum(np.diff(a, axis=0)**2, axis=1)), [0]))
    
    return j
