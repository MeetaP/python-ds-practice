def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_phrase = "" 
    for i in phrase:
        if i.casefold() == to_swap.casefold():
            if i.islower():
                flipped_phrase += i.upper()
            else:
                flipped_phrase += i.lower()
        else:
            flipped_phrase += i
    return flipped_phrase

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))