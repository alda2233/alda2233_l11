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
from functions import generate_matrix_char
# Constants


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = generate_matrix_char(rows, cols)

for row in matrix:
    print(row)
