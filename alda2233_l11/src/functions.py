"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
import random

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """

    if value_type == "float":
        generate_random = random.uniform
    elif value_type == "int":
        generate_random = random.randint
    else:
        raise ValueError("Invalid value_type. Use 'float' or 'int'.")

    matrix = [[generate_random(low, high)
               for _ in range(cols)] for _ in range(rows)]
    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    matrix = [[random.choice(alphabet) for _ in range(cols)]
              for _ in range(rows)]
    return matrix


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    word_length = len(word_list[0])
    if not all(len(word) == word_length for word in word_list):
        raise ValueError("All words in the list must have the same length.")

    matrix = [list(word) for word in word_list]
    return matrix


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    if not matrix or not matrix[0]:
        raise ValueError("Matrix must not be empty.")

    # Initialize with the first element
    smallest = largest = matrix[0][0]
    total = 0  # Correct initialization

    # Calculate statistics
    num_elements = 0
    for row in matrix:
        for num in row:
            total += num
            smallest = min(smallest, num)
            largest = max(largest, num)
            num_elements += 1

    # Calculate average
    if num_elements > 0:
        average = total / num_elements
    else:
        average = 0

    return smallest, largest, total, average


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= num

    return None
