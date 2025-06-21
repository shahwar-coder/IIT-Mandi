'''
🧠 PROBLEM STATEMENT:
Given a 2D list `arr` with `N` rows and `M` columns, print the **sum of even numbers only** for each row.

✅ Examples:

>>> arr = [[1, 2, 3, 4], [5, 6, 7, 8]]
>>> solve(2, 4, arr)
6
14

Explanation:
- Row 1: 2 and 4 are even → 2 + 4 = 6
- Row 2: 6 and 8 are even → 6 + 8 = 14

📝 Assumptions:
- The matrix is rectangular: each row has exactly M integers
- Only even integers (divisible by 2) are summed
'''

def solve(N, M, arr):
    for row in arr:
        # Sum only the even elements in the current row
        print(sum(elem for elem in row if elem % 2 == 0))
