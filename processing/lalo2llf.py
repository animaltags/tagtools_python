""" Convert latitude-longitude track points into a local level frame

    :param trk: A data frame, two-column matrix, two-element vector  of track points c(latitude, longitude) or sensor data  structure.
    :type: vector or matrix
    :param pt: c(latitude, longitude) of the centre point of the local level frame. If pt is not given, the first point in the track will be used.
    :type: array or vector

    :returns: An array with  northing and easting of track points in the local level frame. Northing and easting are in metres. The axes of the frame are true (geographic) north and true east.
    :rtype: array

    Example: coordinates = np.array([[-122.4194, 37.7749], [-73.9352, 40.7306]])
        lalo2llf(coordinates, [15, 19])
    Returns: [[-15270043.728        2015179.06765092]
            [ -9882479.424        2332425.21917534]]

    Valid: Python
    oko2@calvin.edu
    Last modified: 29 June 2023
    """

import numpy as np

def lalo2llf(trk, pt=None):
    if isinstance(trk, list):
        if 'data' in trk and 'depid' in trk:
            trk = trk['data'][:, 2:4]

        if isinstance(trk, np.ndarray):
            trk = trk.astype(float)
        else:
            trk = np.array(trk).astype(float)

    if pt is None:
        pt = trk[0]

    trk = trk - np.tile(pt, (trk.shape[0], 1))

    northing = trk[:, 0] * 1852 * 60
    easting = trk[:, 1] * 1852 * 60 * np.cos(pt[0] * np.pi / 180)
    NE = np.column_stack((northing, easting))

    return NE