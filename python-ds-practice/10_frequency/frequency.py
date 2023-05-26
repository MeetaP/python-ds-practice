def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    freq_dict = {}

    for i in lst:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    for key, val in freq_dict.items():
        if search_term in freq_dict:
            return freq_dict[i]
        else:
            return 0
        
print(frequency([1, 4, 3, 4, 4], 4))
print(frequency([1, 4, 3], 7))