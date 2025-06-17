'''
🧠 PROBLEM STATEMENT:
Given an integer `N` and a string of length `N`, print each character of the string on a new line, **starting from the last character** to the first.

✅ Examples:

>>> print_characters(4, "code")
e
d
o
c

>>> print_characters(6, "hello!")
!  
o  
l  
l  
e  
h  

📝 Assumption:
- The string has exactly `N` characters.
'''

def print_characters(N, string):
    # Iterate through the string in reverse order and print each character
    for i in string[::-1]:  # string[::-1] reverses the string
        print(i)
