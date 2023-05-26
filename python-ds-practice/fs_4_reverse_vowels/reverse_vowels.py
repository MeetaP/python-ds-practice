def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    new_list = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if new_list[i].lower() not in ('a', 'e', 'i', 'o', 'u'):
            i += 1
        elif new_list[j].lower() not in ('a', 'e', 'i', 'o', 'u'):
            j -= 1
        else:
            temp = new_list[i]
            new_list[i] = new_list[j]
            new_list[j] = temp
            i += 1
            j -= 1
    return "".join(new_list)
        

print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("why try, shy fly?"))