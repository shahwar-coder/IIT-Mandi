'''
🧠 PROBLEM STATEMENT:
Recreate the functionality of Python's `"separator".join(list)` method.

Given:
- A list of strings
- A separator string

Return:
- A single string formed by joining the list elements with the given separator.

✅ Example:

>>> imitate_join(["Hello", "Shahwar", "Alam", "Naqvi"], ' ')
'Hello Shahwar Alam Naqvi'

📝 Assumptions:
- The list contains only strings
- Separator is a valid string (including empty string '' if needed)
'''

from typing import List

def imitate_join(strings: List[str], separator: str) -> str:
    """Imitate the behavior of str.join()"""
    sentence = ''
    for i, string in enumerate(strings):
        sentence += string
        # Add the separator after every element except the last one
        if i != len(strings) - 1:
            sentence += separator
    return sentence

# Test case
print(imitate_join(["Hello", "Shahwar", "Alam", "Naqvi"], ' '))  # Output: 'Hello Shahwar Alam Naqvi'
