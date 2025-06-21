'''
🧠 PROBLEM STATEMENT:
Given a 2D list `arr` with `N` rows and `M` columns, print its elements in row-major order.

Each row should be printed on a new line, with elements separated by spaces.

✅ Examples:

>>> arr = [[1, 2, 3], [4, 5, 6]]
>>> solve(arr, 2, 3)
1 2 3 
4 5 6 

📝 Assumptions:
- arr is a list of lists, where each sublist represents a row
- Each row has exactly M elements
'''

def solve(arr, N, M):
    for i in arr:  # Loop through each row
        for j in i:  # Loop through each element in the row
            print(j, end=" ")  # Print element with space
        print()  # Move to the next line after each row
