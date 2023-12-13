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
from functions import matrix_scalar_multiply
# Constants

rows = int(input("Enter the number of rows (positive integer): "))
cols = int(input("Enter the number of columns (positive integer): "))

if rows <= 0 or cols <= 0:
    print("Number of rows and columns must be positive integers.")
    exit()

matrix = []
for i in range(rows):
    row = [float(input(f"Enter element {i+1},{j+1}: ")) for j in range(cols)]
    matrix.append(row)


num = float(input("Enter the scalar value: "))


matrix_scalar_multiply(matrix, num)


print("Result after scalar multiplication:")
for row in matrix:
    print(row)
