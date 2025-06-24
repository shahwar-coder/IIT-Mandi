'''
🧠 PROBLEM STATEMENT:
Given a 2D list `arr` with `N` rows and `M` columns, print the sum of **odd numbers only** for each row.

✅ Example:

>>> arr = [[1, 2, 3], [4, 5, 6]]
>>> solve(2, 3, arr)
4
5

Explanation:
- Row 1: 1 and 3 are odd → 1 + 3 = 4
- Row 2: 5 is odd → sum = 5

📝 Assumptions:
- `arr` is a list of lists with dimensions N x M
- Each sublist (row) contains exactly M integers
'''

def solve(N, M, arr):
    for row in arr:
        # Use a generator expression to filter and sum only odd numbers
        print(sum(elem for elem in row if elem % 2 != 0))
