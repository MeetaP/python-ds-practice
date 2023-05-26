def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    dict_alnum = {}

    if len(keys) == len(values) or len(values) > len(keys):
        dict_alnum = {key:val for key, val in zip(keys,values)}
    elif len(keys) > len(values):
        i = 0
        j = 0
        while i <= len(keys) - 1:
            while j <= len(values) - 1:
                dict_alnum[keys[i]] = values[j]
                i += 1
                j += 1
            dict_alnum[keys[i]] = None
            i += 1
    return dict_alnum


print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))