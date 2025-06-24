'''
🧠 PROBLEM STATEMENT:
Given a list of integers, return the **minimum value** in the list.

✅ Example:

>>> findMinMax([15, 2, 34, 8, 19])
2

📝 Assumptions:
- The list contains at least one integer.
- No need to handle empty lists unless explicitly required.
'''

from typing import List

def findMinMax(arr: List[int]) -> int:
    return min(arr)

# Test case
print(findMinMax([15, 2, 34, 8, 19]))  # Output: 2
