'''
🧠 PROBLEM STATEMENT:
Given an integer `n`, check if the number contains the sequence `420` **anywhere** in its digits.

If the sequence `420` is present, print `"Caught"`.
Otherwise, print `"Escaped"`.

✅ Examples:

>>> Solve(124203)
Caught

>>> Solve(123456)
Escaped

>>> Solve(420)
Caught
'''

def Solve(n):
    # Convert number to string so we can search for digit patterns
    str_420 = '420'

    # Check if '420' exists in the string version of the number
    if str_420 in str(n):
        print("Caught")
    else:
        print("Escaped")
