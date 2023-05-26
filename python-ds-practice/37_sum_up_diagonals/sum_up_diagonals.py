def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum_diagonal_TL_to_BR = 0
    sum_diagonal_BL_to_TR = 0

    for ind in range(len(matrix)):
        sum_diagonal_TL_to_BR += matrix[ind][ind]
        sum_diagonal_BL_to_TR += matrix[ind][len(matrix)-1-ind]
    return sum_diagonal_TL_to_BR + sum_diagonal_BL_to_TR

m1 = [
        [1, 2],
        [30, 40],
    ]
print(sum_up_diagonals(m1))

m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
      ]
print(sum_up_diagonals(m2))