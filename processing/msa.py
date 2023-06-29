"""This function is used to compute the Minimum Specific Acceleration (MSA). This is the absolute value of the norm of the acceleration minus 1 g, i.e., the amount that the acceleration differs from the gravity value. This is always equal to or less than the actual specific acceleration if A is correctly calibrated.

    :param A: A An nx3 acceleration matrix with columns [ax ay az], or a tag sensor data list containing acceleration data. Acceleration can be in any consistent unit, e.g., g or m/s^2. A can be in any frame as the MSA is rotation independent.
    :type: matrix
    :param ref: The gravitational field strength in the same units as A. This is not needed if A is a sensor structure. If A is a matrix, the default value is 9.81 which assumes that A is in m/s^2. Use ref = 1 if the unit of A is g.
    :type: scalar or vector

    :returns: A: A column vector of MSA with the same number of rows as A, or a tag sensor data list (output matches input). m has the same units as A.
    :rtype: vector

    Example: matrix = np.array([[1, -0.5, 0.1], [0.8, -0.2, 0.6], [0.5, -0.9, -0.7]])
            msa(matrix, 1)
    Returns: [0.12249722 0.0198039  0.24498996]

    Valid: Python
    oko2@calvin.edu
    Last modified: 29 June 2023
    """

import datetime
import numpy as np

def msa(A, ref):
    # input checks
    if ref is None:
        ref = 9.81
    
    if isinstance(A, list):
        if 'meta_conv' in A and len(A['meta_conv']) > 0:
            ref = ref * A['meta_conv']
        
        if 'data' in A:
            A0 = A
            A = A['data']
        else:
            A = np.asarray(A)
    
    if np.min([A.shape[0], A.shape[1]]) == 1:
        raise ValueError("A must be an acceleration matrix")
    
    m = np.abs(np.sqrt(np.sum(A**2, axis=1)) - ref)
    
    if 'A0' in locals():
        M = A0
        M['data'] = m
        M['creation_date'] = datetime.datetime.now()
        M['type'] = 'msa'
        M['full_name'] = 'minimum specific acceleration'
        M['description'] = M['full_name']
        M['column_name'] = 'msa'
        return M
    else:
        return m