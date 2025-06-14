'''
🧠 PROBLEM STATEMENT:
Given an integer `N`, print a **right-shifting inverted triangle** of asterisks (`*`), 
aligned with decreasing stars on the left and increasing spacing on the right.

✅ Examples:

>>> solve(5)
* * * * * 
* * * *   
* * *     
* *       
*         

Explanation:
- The first row has 5 stars
- Each next row has 1 fewer star and 2 more spaces on the right

This gives a **right-slanting** effect due to spaces at the end.
'''

def solve(N):
    for i in range(N):
        # '* ' has one asterisk and one space; used to print stars with spacing
        row = (N - i) * '* '
        print(row.strip(), end='')  # strip to remove trailing space

        # '  ' has **two spaces**; used to create shifting effect by increasing right margin
        right_spaces = i * '  '
        print(right_spaces)  # moves to next line
