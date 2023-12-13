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
from functions import words_to_matrix
# Constants

word_list = input("Enter words separated by spaces: ").split()


matrix = words_to_matrix(word_list)


for row in matrix:
    print(row)
