'''
🧠 PROBLEM STATEMENT:
Given an integer `N` and a string of length `N`, print every second character of the string starting from index 0 (i.e., characters at even indices).

✅ Examples:

>>> print_characters(6, "abcdef")
a
c
e

>>> print_characters(5, "hello")
h
l
o

📝 Assumptions:
- The string has exactly `N` characters.
- Indexing starts from 0.
'''

def print_characters(N, string):
    # Loop through even indices (0, 2, 4, ...) and print the characters
    for i in range(0, len(string), 2):
        print(string[i])
