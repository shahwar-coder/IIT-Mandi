'''
🧠 PROBLEM STATEMENT:
Check whether a given string of length `N` is a palindrome.

A palindrome is a string that reads the same forwards and backwards.
We will compare characters from the start and end, moving inward.

✅ Examples:

>>> is_palindrome(5, "madam")
Yes

>>> is_palindrome(6, "coding")
No
'''

def is_palindrome(N, Str):
    # Start two pointers: one from the beginning, one from the end
    left = 0
    right = N - 1

    # Keep checking characters until the pointers meet or cross
    while left < right:
        # If characters at current positions don't match, it's not a palindrome
        if Str[left] != Str[right]:
            print("No")
            return  # Exit early if mismatch is found

        # Move both pointers toward the center
        left += 1
        right -= 1

    # If loop completes with no mismatches, it's a palindrome
    print("Yes")


# Below what you see was my first approach.
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
