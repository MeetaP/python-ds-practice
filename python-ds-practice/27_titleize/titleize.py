def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    list_words = phrase.split(" ")
    for ind, word in enumerate(list_words):
        list_words[ind] = word[0].upper() + word[1:].lower()
    
    return list_words

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
