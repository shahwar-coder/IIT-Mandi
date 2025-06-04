'''
🧠 PROBLEM STATEMENT:
Given an integer `N`, classify it based on its divisibility:

- If N is divisible by both 4 and 6 → print "Awesome!"
- If only divisible by 4          → print "Four!"
- If only divisible by 6          → print "Six!"
- If divisible by neither         → print "Dark!"

✅ Examples:

>>> Solve(12)
Awesome!
# 12 is divisible by both 4 and 6

>>> Solve(8)
Four!
# 8 is divisible by 4 only

>>> Solve(18)
Six!
# 18 is divisible by 6 only

>>> Solve(7)
Dark!
# 7 is divisible by neither
'''
def Solve(N):
    # Check divisibility by both 4 and 6 first
    if N % 4 == 0 and N % 6 == 0:
        print("Awesome!")
    # Then check if only divisible by 4
    elif N % 4 == 0:
        print("Four!")
    # Then check if only divisible by 6
    elif N % 6 == 0:
        print("Six!")
    # If none of the above, print fallback case
    else:
        print("Dark!")
