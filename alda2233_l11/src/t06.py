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
from functions import matrix_stats
# Constants
print("Enter the matrix values. Type 'done' when finished.")
matrix = []
while True:
    row_input = input(
        "Enter a row (space-separated values) or 'done' to finish: ")
    if row_input.lower() == 'done':
        break
    row = [float(value) for value in row_input.split()]
    matrix.append(row)


smallest, largest, total, average = matrix_stats(matrix)


print("\nMatrix Statistics:")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Total: {total}")
print(f"Average: {average}")
