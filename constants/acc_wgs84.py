def acc_wgs84(l=None):
    """Calculates the total acceleration due to gravitation and centripetal force at the earth's surface according to the WGS84 international gravity formula.

    :param l: latitude in degrees
    :type: scalar or vector
    :param T: temperature in degrees C
    :type: scalar or vector
    :param d: depth in meters
    :type: scalar or vector
    Input arguments can be scalars, or a mixture of vectors and scalars as long as each argument is either a vector of length nx1 (with n being the same for all vector arguments) or a scalar.

    :raises NameError: if you input less than three arguments, the function will not accept it. 
        All three are required.

    :returns: g: given in units of m/s^2
    :rtype: scalar, if all inputs were scalars. If one or more were vectors, return is a vector.

    Example: acc_wgs84(50)
    Returns: 9.8107 $m/s^2$

    Valid: Python
    oko2@calvin.edu
    Last modified: 22 May 2023
    """

    g = 0
    if not l:
        help(acc_wgs84)
        return g
        return
    import math 
    latrad = l * math.pi/180
    g = 9.7803267714 * (1 + 0.0019318514 * math.sin(latrad)**2) / math.sqrt(1 - 0.00669438 * math.sin(latrad)**2)
    return g
    return

acc_wgs84()