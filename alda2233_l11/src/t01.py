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
from functions import generate_matrix_num
# Constants
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
low = float(input("Enter the low value of the range: "))
high = float(input("Enter the high value of the range: "))
value_type = input("Enter the type of values ('float' or 'int'): ")

matrix = generate_matrix_num(rows, cols, low, high, value_type)

for row in matrix:
    print(row)
