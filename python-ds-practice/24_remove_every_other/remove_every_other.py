def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    even_index_list = []

    for index, number in enumerate(lst):
        if index % 2 == 0:
            even_index_list.append(number)
    return even_index_list

lst = [1, 2, 3, 4, 5]
print(remove_every_other(lst))
