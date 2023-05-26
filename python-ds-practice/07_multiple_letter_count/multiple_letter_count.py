def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    freq_dict = {}

    for i in phrase:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))