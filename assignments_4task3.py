#! /usr/bin/env python


from __future__ import division, print_function


def matrix_mul(matr1, matr2):
    ''' Calculates the result of multiplication of two matrices
    :type matr1: list
    :param matr1: list of lists integer or float numbers
    :type matr2: list
    :param matr2: list of lists integer or float numbers
    :return:
    '''
    nrow_matr1, ncol_matr1 = len(matr1), len(matr1[0])
    nrow_matr2, ncol_matr2 = len(matr2), len(matr2[0])
    if ncol_matr1 != nrow_matr2:
        raise ValueError("Matrices are of incorrect length")
    matrix_mult_res = [[None for j in xrange(ncol_matr2)]
                       for i in xrange(nrow_matr1)]

    def vector_mult(row, col):                                              # multiple row on a column
        if len(row) != len(col):
            raise ValueError("Vectors can not be multiplied")
        res = 0
        for i in xrange(len(row)):
            if not (isinstance(row[i], (int, float)) and isinstance(col[i], (int, float))):
                raise ValueError("Invalid data format")
            res += row[i]*col[i]
        return res

    def get_col(matr, j):
       return [row[j] for row in matr]

    for i in xrange(nrow_matr1):
        for j in xrange(ncol_matr2):
            matrix_mult_res[i][j] = vector_mult(matr1[i], get_col(matr2, j))
    return matrix_mult_res

matr1 = [[1,2,3], [1,2,3], [1,2,3]]
matr2 = [[1,2], [2,1], [0,5]]
print(matrix_mul(matr1, matr2))

# matr1 = [[1,2,3]]
# matr2 = [[1], ['a'], [3]]
# print(matrix_mul(matr1, matr2))

matr1 = [[1,2,3], [1,2,5.2], [1,2,3]]
matr2 = [[1,2], [2,1], [0,5]]
print(matrix_mul(matr1, matr2))