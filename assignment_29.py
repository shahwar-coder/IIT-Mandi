'''
🧠 PROBLEM STATEMENT:
Given a 2D matrix `arr` of size `N x M`, print the sum of the **first and last elements** of every row.

✅ Example:

>>> arr = [
...   [1, 2, 3],
...   [4, 5, 6],
...   [7, 8, 9]
... ]
>>> solve(3, 3, arr)
30

Explanation:
- Row 1: 1 + 3 = 4
- Row 2: 4 + 6 = 10
- Row 3: 7 + 9 = 16
- Total sum = 4 + 10 + 16 = 30
'''

def solve(N, M, arr):
    total = 0
    for row in arr:
        # Add first and last elements of the current row
        total += row[0] + row[-1]
    print(total)
