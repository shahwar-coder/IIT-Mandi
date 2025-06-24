'''
🧠 PROBLEM STATEMENT:
Write a function `manual_reverse` that manually reverses a string or a list without using
slicing (`[::-1]`) or built-in `reversed()`.

- If the input is a string, return the reversed string.
- If the input is a list (of int or str), return the reversed list.

✅ Examples:

>>> manual_reverse([1, 2, 3])
[3, 2, 1]

>>> manual_reverse('Shahwar')
'rawhahS'
'''

from typing import List, Union

def manual_reverse(items: Union[List[Union[int, str]], str]) -> Union[List[Union[int, str]], str]:
    result = []
    for item in items:
        result.insert(0, item)  # Insert at front each time
    return ''.join(result) if isinstance(items, str) else result


# Test cases
print(manual_reverse([1, 2, 3, 4, 5]))       # [5, 4, 3, 2, 1]
print(manual_reverse(['1', '2', '3']))       # ['3', '2', '1']
print(manual_reverse('Shahwar'))            # 'rawhahS'

'''
📌 NOTES ON EFFICIENCY & BEHAVIOR:

- This approach uses `insert(0, item)` in a loop, which is **O(n)** for each insertion.
- Total time complexity becomes **O(n²)** for lists.
- For strings, this is fine since we rebuild using `''.join()` (which is O(n)).

⚠️ Less efficient for large lists. Prefer alternatives in real-world code:
- `items[::-1]` (slicing)
- `list(reversed(items))` for lists
- `''.join(reversed(string))` for strings

✅ Best used for educational purposes to understand the reversing mechanism.
'''
