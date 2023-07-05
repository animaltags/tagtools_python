""" Merge the fields of two lists

    :param s1: Arbitrary list e.g., containing metadata or settings.
    :type: dict
    :param s2: Arbitrary list e.g., containing metadata or settings.
    :type: dict

    :returns: A list containing all of the fields in s1 and s2
    :rtype: list

    Example: s1 = {"a": 1, "b": [2, 3, 4]}
        s2 = {"b": 3, "c": "cat"}
        merge_fields(s1,s2)
    Returns: {'a': 1, 'b': [2, 3, 4], 'c': 'cat'}

    Valid: Python
    oko2@calvin.edu
    Last modified: 29 June 2023
    """

def merge_fields(s1, s2):
    if s1 is None or s2 is None:
        raise ValueError("Inputs for both s1 and s2 are required")

    if not isinstance(s1, dict) or not isinstance(s2, dict):
        raise TypeError("Both inputs must be dictionaries in merge_fields")

    s = s2.copy()
    s.update(s1)
    s = {k: v for k, v in s.items() if list(s.values()).count(v) == 1}
    s = {k: v for k, v in sorted(s.items())}

    return s