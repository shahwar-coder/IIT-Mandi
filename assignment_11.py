'''
🧠 PROBLEM STATEMENT:
Given a positive integer `N`, print a left-aligned triangle of asterisks `*`,
with `N` rows. Each row `i` should contain `i` asterisks.

✅ Examples:

>>> print_pattern(3)
*
**
***

>>> print_pattern(5)
*
**
***
****
*****

This forms a simple increasing triangle of stars.
'''

def print_pattern(N):
    for i in range(1, N + 1):
        print("*" * i)  # Print i asterisks in the ith row
