import numpy as np
rows = int(input("enter number of rows: "))
cols = int(input("enter number of columns: "))
matrix = []
print("enter elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"enter element at position [{i+1}][{j+1}]: "))
        row.append(val)
    matrix.append(row)

print("\noriginal matrix:")
for r in matrix:
    print(r)

arr = np.array(matrix)
rank = np.linalg.matrix_rank(arr)
print("\nRank of the matrix:", rank)
