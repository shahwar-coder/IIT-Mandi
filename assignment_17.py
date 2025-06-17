'''
🧠 PROBLEM STATEMENT:
Given an integer `N` and a string of length `N`, print each character of the string on a new line.

✅ Examples:

>>> print_characters(4, "code")
c
o
d
e

>>> print_characters(6, "hello!")
h
e
l
l
o
!

📝 Assumption:
- The string is guaranteed to have length `N`.
'''

def print_characters(N, string):
    # Loop through each character and print on a new line
    for char in string:
        print(char)
