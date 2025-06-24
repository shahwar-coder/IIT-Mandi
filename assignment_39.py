'''
🧠 PROBLEM STATEMENT:
Create a custom function to replicate string slicing behavior: `s[start:end]`

Given:
- A string `s`
- Start index `start`
- End index `end` (non-inclusive)

Return:
- A new substring starting from `start` index up to but not including `end`

✅ Examples:

>>> custom_substring("Shahwar", 0, 4)
'Shah'

>>> custom_substring("Python", 2, 5)
'tho'

📝 Assume:
- `start` and `end` are valid indices
- No need to handle negative indices or index errors yet
'''

def custom_substring(s, start, end):
    result = ''
    for i in range(start, end):
        result += s[i]
    return result

# Test cases
print(custom_substring("Shahwar", 0, 4))  # Output: 'Shah'
print(custom_substring("Python", 2, 5))   # Output: 'tho'

'''
📌 NOTES ON LOGIC & EFFICIENCY:

🔍 How it works:
- Loop from index `start` to `end - 1`
- Concatenate each character to `result`

🕒 Time Complexity: O(n), where n = end - start
🧠 Space Complexity: O(n), since strings are immutable and a new string is built

⚠️ Limitations:
- Doesn't support negative indexing or slicing with step
- Repeated string concatenation can be slower for large strings (due to immutability)

✅ Educational value:
- Helps reinforce how Python handles slice-based indexing
- Great stepping stone toward building more advanced text manipulation utilities
'''
