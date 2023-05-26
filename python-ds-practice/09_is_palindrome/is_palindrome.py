def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    reverse_phrase = phrase[::-1].lower()
    reverse_phrase_clean = "".join(i for i in reverse_phrase if i.isalnum())
    orig_phrase = "".join(i for i in phrase if i.isalnum())
    if orig_phrase.lower() == reverse_phrase_clean:
        return True
    else:
        return False
    
print(is_palindrome('tacocat'))
print(is_palindrome('noon'))
print(is_palindrome('taco cat'))
