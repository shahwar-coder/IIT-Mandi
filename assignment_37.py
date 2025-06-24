'''
🧠 PROBLEM STATEMENT:
Create a custom function that mimics the behavior of `str.find()`, which returns the index
of the first occurrence of a given `substring` in a `string`.

- Return the index where the substring first appears.
- If the substring is not found, return -1.

✅ Examples:
>>> custom_find("Shahwar Naqvi", "Naq")
8

>>> custom_find("OpenAI", "pen")
1

>>> custom_find("hello", "z")
-1
'''

def custom_find(string: str, substring: str) -> int:
    "Custom Substring finding function"
    length_of_string = len(string)
    length_of_substring = len(substring)

    for i in range(length_of_string - length_of_substring + 1):
        # Fix: compare from i to i + length_of_substring
        if string[i:i + length_of_substring] == substring:
            return i
    return -1


# Test cases
print(custom_find("Shahwar Naqvi", "Naq"))  # 8
print(custom_find("OpenAI", "pen"))         # 1
print(custom_find("hello", "z"))            # -1

'''
📌 NOTES ON LOGIC & EFFICIENCY:

🔍 How it works:
- For each possible starting index `i` in `string`, we check if the slice `string[i:i+len(substring)]`
  matches the `substring`.
- We only go up to `len(string) - len(substring)` to avoid index overflow.

🕒 Time Complexity:
- Worst-case: **O(n × m)** where:
  - `n` is length of `string`
  - `m` is length of `substring`

✅ This mimics how a basic substring search works before using optimized algorithms like:
- KMP (Knuth-Morris-Pratt)
- Rabin-Karp
- Boyer-Moore

✅ Best used for learning and small-scale problems.
'''
