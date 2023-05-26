def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    check_list = False

    for item in lst:
        if isinstance(item, list):
            check_list = True
        else:
            check_list = False
    return check_list

print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))

