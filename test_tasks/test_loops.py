"""Loop exercises focusing on iteration and nested loops.

Seven holes: six single-line TODOs and one final small block to print results.
Hints: use `for` loops, `range()`, indexing, and list `.append()`.
"""

# A simple 3x3 matrix for students to work with
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# 1) number of rows
# TODO: fill this line
rows = None  # TODO: replace None with len(matrix)

# 2) number of columns (assume rectangular)
# TODO: fill this line
cols = None  # TODO: replace None with len(matrix[0])

# 3) initialize flattened list
# TODO: fill this line
flat = None  # TODO: replace None with []

# 4) nested loop: append each value from matrix into flat
for i in range(rows):
    for j in range(cols):
        val = matrix[i][j]
        # TODO: fill this line to append value into flat
        flat.append(None)  # TODO: replace None with val

# 5) compute sum of flattened values
# TODO: fill this line
sum_flat = None  # TODO: replace None with sum(flat)

# 6) prepare a list of pairs (i,j) for values > 5
# TODO: fill this line
pairs = None  # TODO: replace None with []
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > 5:
            pairs.append((i, j))

# Final small block (1-3 lines): compute average and print results
# TODO: complete the block below
average = None  # TODO: replace None with sum_flat / len(flat)
print("flat:", flat)
print("sum:", sum_flat, "average:", average)
