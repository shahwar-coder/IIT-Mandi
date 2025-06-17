'''
🧠 PROBLEM STATEMENT:
Given an integer `N` and a string `Str` of length `N`, determine if the string is a **palindrome**.
A palindrome is a string that reads the same forward and backward.

✅ Examples:

>>> is_palindrome(5, "madam")
Yes

>>> is_palindrome(6, "python")
No

>>> is_palindrome(1, "a")
Yes

📝 Assumptions:
- The string has exactly `N` characters.
- The check is **case-sensitive** (e.g., "Madam" is not equal to "madam").
- No preprocessing is done (punctuation, spaces, etc., are not ignored).
'''

def is_palindrome(N, Str):
    # A string is a palindrome if it's equal to its reverse
    if Str == Str[::-1]:  # Str[::-1] creates a reversed version of the string
        print("Yes")
    else:
        print("No")
