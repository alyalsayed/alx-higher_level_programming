#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use a list comprehension to compute the square of each element in the matrix
    result = [[item ** 2 for item in row] for row in matrix]
    
    # Return the new matrix
    return result

