'''
🧠 PROBLEM STATEMENT:
Given a 2D list `arr` with `N` rows and `M` columns, print the **sum of each row** on a separate line.

✅ Examples:

>>> arr = [[1, 2, 3], [4, 5, 6]]
>>> solve(2, 3, arr)
6
15

📝 Assumptions:
- `arr` is a list of lists.
- Each sublist has exactly `M` integers.
'''

def solve(N, M, arr):
    for a in arr:
        print(sum(a))  # Sum the row and print it
