def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    dedup_dict = {}

    for i in nums:
        if i in dedup_dict:
            dedup_dict[i] += 1
        else:
            dedup_dict[i] = 1
    
    for key, value in dedup_dict.items():
        if dedup_dict.get(key) > 1:
            return key
    return None

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
print(find_the_duplicate([2, 1, 3, 4]))

