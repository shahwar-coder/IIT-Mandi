'''
🧠 PROBLEM STATEMENT:
Given a list `arr` of length `size`, print its elements in **reverse order** on a single line, separated by spaces.

✅ Examples:

>>> reverse_traversal(5, [1, 2, 3, 4, 5])
5 4 3 2 1 

>>> reverse_traversal(3, [10, 20, 30])
30 20 10 

📝 Assumptions:
- The list contains `size` elements.
'''

def reverse_traversal(size, arr):
    # Traverse and print elements from the end using slicing
    for elem in arr[::-1]:
        print(elem, end=' ')
