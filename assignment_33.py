'''
🧠 PROBLEM STATEMENT:
Write a function that takes a string as input and returns its **reverse**.

✅ Example:

>>> reverseString("Shahwar")
'rawhahS'

📝 Assumptions:
- The input is a valid non-empty string
- The reversal should preserve the original character cases
'''

def reverseString(string: str) -> str:
    # Use slicing to reverse the string: [start:stop:step]
    return string[::-1]

# Test case
print(reverseString(string="Shahwar"))  # Output: 'rawhahS'
