import pandas as pd

def sound_speed(T=None, D=None, S=None):
    """This function is used to estimate the sound speed using Coppens equation

    :param T: Temperature in degrees
    :type: scalar or vector
    :param S: The salinity in part-per-thousand (defaults to 35 ppt)
    :type: scalar or vector
    :param D: (optional) The depth in meters (defaults to 1 m)
    :type: scalar or vector
    Input arguments can be scalars, or a mixture of vectors and scalars as long as each argument is either a vector of length nx1 (with n being the same for all vector arguments) or a scalar.

    :raises NameError: if you input less than three arguments, the function will not accept it. 
        All three are required.

    :returns: v: The sound speed in m/s
    :rtype: scalar, if all inputs were scalars. If one or more were vectors, return is a vector.

    Example: sound_speed(8, 1000, 34) 
    Returns: 1497.7 m/s

    Valid: Python
    oko2@calvin.edu
    Last modified: 22 May 2023
    """

    p = 0
    if not T:
        help(sound_speed)
        return p
    if pd.isnull(D):
        D = 1
    if pd.isnull(S):
        S = 35
    

    t = T / 10
    D = D / 1000
    v0 = 1449.05 + 45.7 * t - 5.21 * t**2 + 0.23 * t**3 + (1.333 - 0.126 * t + 0.009 * t**2) * (S - 35)
    v = v0 + (16.23 + 0.253 * t) * D + (0.213 - 0.1 * t) * D**2 + (0.016 + 0.0002 * (S - 35)) * (S - 35) * t * D
    return v

sound_speed()