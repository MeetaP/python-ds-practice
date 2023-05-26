def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    freq_dict_1 = {}
    freq_dict_2 = {}
    
    for i in str(num1):
        if i not in freq_dict_1:
            freq_dict_1[i] = 1
        else:
            freq_dict_1[i] += 1
    
    for i in str(num2):
        if i not in freq_dict_2:
            freq_dict_2[i] = 1
        else:
            freq_dict_2[i] += 1
    
    if len(freq_dict_1) != len(freq_dict_2):
        return False

    equality_check = 0
    for i in freq_dict_1:
        if freq_dict_1.get(i) != freq_dict_2.get(i):
            equality_check = 1
            break
    if equality_check == 0:
        return True
    else:
        return False

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))