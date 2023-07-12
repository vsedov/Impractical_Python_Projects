"""Find palindromes (letter palingrams) in a dictionary file."""


import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

pali_list = [
    word for word in word_list if len(word) > 1 and word == word[::-1]
]
print(f"\nNumber of palindromes found = {len(pali_list)}\n")

# print in list format with no quotes or commas:
print(*pali_list, sep='\n')
