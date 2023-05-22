def depth2pressure(d=None, l=None):
    """This function is used to convert the depth (in meters) to the pressure in Pascals.

    :param l: latitude in degrees
    :type: scalar or vector
    :param d: depth in meters
    :type: scalar or vector
    Input arguments can be scalars, or a mixture of vectors and scalars as long as each argument is either a vector of length nx1 (with n being the same for all vector arguments) or a scalar.

    :raises NameError: if you input less than two arguments, the function will not accept it. 
        All two are required.

    :returns:p: The pessure in Pa
    :rtype: scalar, if all inputs were scalars. If one or more were vectors, return is a vector.

    Example: depth2pressure(1000, 27)
    Returns: 10075403 Pa

    Valid: Python
    oko2@calvin.edu
    Last modified: 22 May 2023
    """

    p = 0
    if not l:
        help(depth2pressure)
        return p
    if not d:
        print("Error: all inputs required")
        return p
    
    import math 

    thyh0Z = 1e-2 * d / (d + 100) + 6.2e-6 * d
    g = 9.7803 * (1 + 5.3e-3 * math.sin(l * math.pi / 180)**2)
    k = (g - 2e-5 * d) / (9.80612 - 2e-5 * d)
    hZ45 = 1.00818e-2 * d + 2.465e-8 * d**2 - 1.25e-13 * d**3 + 2.8e-19 * d**4
    p = 1e6 * (hZ45 * k - thyh0Z)
    return p

depth2pressure()