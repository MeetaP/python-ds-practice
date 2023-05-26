def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    dict_vowels = {}

    for letter in phrase:
        if letter.casefold() in ('a', 'e', 'i', 'o', 'u'):
            if letter.casefold() in dict_vowels:
                dict_vowels[letter.casefold()] += 1
            else:
                dict_vowels[letter.casefold()] = 1
    return dict_vowels

print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))