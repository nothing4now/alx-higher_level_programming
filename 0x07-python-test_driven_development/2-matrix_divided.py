def matrix_divided(matrix, div):
    # check if matrix is a list of lists of integers or floats
    if not all(isinstance(inner_list, list) and all(isinstance(i, (int, float)) for i in inner_list) for inner_list in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # check if all rows of the matrix are of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    # check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # create a new matrix to store the divided values
    divided_matrix = []

    # iterate over the rows of the matrix
    for row in matrix:
        # create a new row to store the divided values
        divided_row = []

        # iterate over the elements in the row
        for element in row:
            # divide the element by the divisor, round to 2 decimal places, and append it to the new row
            divided_row.append(round(element / div, 2))

        # append the divided row to the new matrix
        divided_matrix.append(divided_row)

    # return the new matrix
    return divided_matrix

