def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_phrase = ""
    new_phrase = phrase[0].upper() + phrase[1:]
    return new_phrase

print(capitalize('python'))

print(capitalize('only first word'))
