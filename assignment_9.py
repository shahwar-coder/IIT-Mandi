'''
🧠 PROBLEM STATEMENT:
Given an integer `num`, print a square grid of numbers from 1 to `num`, repeated in each row.

Each row contains numbers from 1 to `num`, and there are `num` such rows.

✅ Examples:

>>> print_number_grid(3)
1 2 3 
1 2 3 
1 2 3 

>>> print_number_grid(5)
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 

'''

def print_number_grid(num):
    # Loop over each row
    for i in range(1, num + 1):
        # For each row, print numbers from 1 to num
        for j in range(1, num + 1):
            print(f"{j} ", end='')  # Print on same line with space
        print()  # Move to next line after each row
