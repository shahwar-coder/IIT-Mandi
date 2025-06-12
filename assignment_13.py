'''
1. What is multidimentional List in Python?
Ans.
A multidimensional list in Python is a list that contains other lists as elements.
It is often used to represent matrices or tables.

Example:
matrix = [[1, 2], [3, 4]]

2. Output ?
matrix = [[10, 20], [30, 40]]
print(matrix[0][1])
Ans.
20

3. How to initialize 3x3 matrix filled with zeroes?
Ans.
matrix = [[0 for _ in range(3)] for _ in range(3)]

4. How to print all elements in a single line, from a 2D matrix?
Ans.
matrix = [[1, 2], [3, 4]]
print(*[elem for row in matrix for elem in row])

5. What is the correct way to access the last element of a 2D matrix?
Ans.
matrix[-1][-1]

6. How to effectively Transpose a Matrix?
Ans.
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [list(row) for row in zip(*matrix)]
print(transposed)

7. How to iterate through both row and column indices in a 2D list?
Ans.
matrix = [[1, 2], [3, 4]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

8. Solve:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = [row[::-1] for row in matrix]
print(new_matrix)
Ans.
[[3, 2, 1], [6, 5, 4], [9, 8, 7]]
'''
