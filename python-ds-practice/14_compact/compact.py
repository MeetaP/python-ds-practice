def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    copy_list = []

    for i in lst:
        if bool(i):
            copy_list.append(i)
    return copy_list

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))