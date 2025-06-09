'''
🧠 PROBLEM STATEMENT:
Print the pattern of the English letter **C**, made of asterisks (`*`), given the height `N`.

- The first and last rows should be fully filled with stars (i.e., `* * * * ...`).
- The middle rows (from row 2 to N-1) should contain only a single star at the beginning.
- The output should visually resemble the capital letter "C".

✅ Examples:

>>> solve(4)
* * * * 
*
*
* * * * 

>>> solve(5)
* * * * * 
*
*
*
* * * * * 

Note: N should be at least 2 for a visible "C" shape.
'''

def solve(N):
    for i in range(N):
        # First and last rows: full row of stars
        if i == 0 or i == N - 1:
            print("* " * N)
        else:
            # Middle rows: only the first star
            print("*")
