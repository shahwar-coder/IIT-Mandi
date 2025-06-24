'''
🧠 PROBLEM STATEMENT:
Create a custom function that mimics Python's built-in slicing `lst[start:end]`.

Given:
- A list `lst`
- Two integers `start` and `end`

Return:
- A **new list** containing elements from index `start` up to but not including `end`.

✅ Examples:

>>> custom_slice([10, 20, 30, 40, 50], 1, 4)
[20, 30, 40]

>>> custom_slice(['a', 'b', 'c', 'd'], 0, 2)
['a', 'b']

📝 Assume:
- `start` and `end` are valid indices (no bounds checking required for now)
'''

def custom_slice(lst, start, end):
    result = []
    for i in range(start, end):
        result.append(lst[i])
    return result

# Test cases
print(custom_slice([10, 20, 30, 40, 50], 1, 4))    # Output: [20, 30, 40]
print(custom_slice(['a', 'b', 'c', 'd'], 0, 2))    # Output: ['a', 'b']

'''
📌 NOTES ON LOGIC & EFFICIENCY:

🔍 How it works:
- Loop through each index `i` from `start` to `end - 1`
- Append `lst[i]` to the result list

✅ This replicates the behavior of Python’s `lst[start:end]` (exclusive of end index)

🕒 Time Complexity: O(n), where n = end - start
🧠 Space Complexity: O(n), for storing the new sublist

⚠️ Limitations:
- Doesn't handle negative indices or out-of-bound errors like Python slicing
- You can extend this to support default `start=0`, `end=len(lst)` behavior if needed
'''
