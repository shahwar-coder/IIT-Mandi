'''
🧠 PROBLEM STATEMENT:
Given a positive integer `N`, print an N×N grid filled with consecutive natural numbers
starting from 1. The numbers should increase **row-wise from left to right**.

✅ Examples:

>>> print_numbers_in_pattern(3)
1 2 3 
4 5 6 
7 8 9 

>>> print_numbers_in_pattern(4)
1  2  3  4 
5  6  7  8 
9 10 11 12 
13 14 15 16

Each row has `N` numbers, and the total count goes up to `N*N`.
'''

def print_numbers_in_pattern(N):
    count = 1  # Start printing from 1
    for i in range(1, N + 1):  # Loop through N rows
        for j in range(1, N + 1):  # Loop through N columns
            print(f"{count} ", end='')  # Print current number with space
            count += 1  # Increment the number
        print()  # Move to the next line after each row
