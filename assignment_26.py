'''
🧠 PROBLEM STATEMENT:
Given a 2D matrix of size `N x M`, print its elements in **zigzag row-wise order**:
- Even-indexed rows (0, 2, 4...) should be printed **in reverse**
- Odd-indexed rows (1, 3, 5...) should be printed **normally (left to right)**

✅ Example:

>>> matrix = [
...   [1, 2, 3],
...   [4, 5, 6],
...   [7, 8, 9]
... ]
>>> solve(3, 3, matrix)
3 2 1 4 5 6 9 8 7 

Explanation:
- Row 0 → reversed → 3 2 1
- Row 1 → normal   → 4 5 6
- Row 2 → reversed → 9 8 7
'''

def solve(N, M, matrix):
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            # Even-indexed row → reverse the row
            for elem in row[::-1]:
                print(elem, end=' ')
        else:
            # Odd-indexed row → print normally
            for elem in row:
                print(elem, end=' ')
