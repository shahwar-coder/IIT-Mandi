'''
🧠 PROBLEM STATEMENT:
Given a string, count and print the number of **consonants** in it.
A consonant is defined as any **alphabet character** that is **not a vowel**.

✅ Examples:

>>> count_consonants("Hello World!")
7

>>> count_consonants("AEIOUaeiou")
0

>>> count_consonants("Python3.8")
5

📝 Assumptions:
- Both uppercase and lowercase vowels should be ignored.
- Only **alphabetic** characters are considered; digits, symbols, and spaces are excluded.
'''

def count_consonants(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # Set of vowels (both cases)
    consonant_count = 0

    for i in string:
        # Check if character is a letter and not a vowel
        if i.isalpha() and i not in vowels:
            consonant_count += 1

    print(consonant_count)
