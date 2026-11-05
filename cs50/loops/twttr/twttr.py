''' this module  removes of vowels'''
letters = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "O"]
result = ""
for c in letters:
    if c in vowels:
        continue
    result += c
print (result)
