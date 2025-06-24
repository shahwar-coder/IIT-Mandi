'''
🧠 PROBLEM STATEMENT:
Given a 2D list `arr` with `N` rows and `M` columns, print a matrix of the same size,
where each element is replaced by the sum of its **row index `i` and column index `j`**.

✅ Example:

>>> arr = [[5, 8], [3, 7]]
>>> solve(2, 2, arr)
0 1
1 2

Explanation:
- At position (0, 0) → 0 + 0 = 0
- At position (0, 1) → 0 + 1 = 1
- At position (1, 0) → 1 + 0 = 1
- At position (1, 1) → 1 + 1 = 2

📝 Assumptions:
- The values in `arr` are not used here — only the dimensions matter.
- Output is based on the **indices**, not the content of the array.
'''

def solve(N, M, arr):
    for i, row in enumerate(arr):  # i = row index
        for j, elem in enumerate(row):  # j = column index
            print(i + j, end=" ")  # Sum of row and column indices
        print()  # Move to next line after each row
