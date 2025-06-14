'''
🧠 PROBLEM STATEMENT:
Given a list of `n` integers, find and print the **maximum** number from the list.

✅ Example:

>>> find_maximum(5, [1, 9, 3, 7, 2])
9

>>> find_maximum(4, [-5, -1, -8, -3])
-1

📝 Assumptions:
- The list `arr` contains exactly `n` integers.
- The list is non-empty.

'''

def find_maximum(n, arr):
    # Print the maximum value in the list using built-in function
    print(max(arr))
