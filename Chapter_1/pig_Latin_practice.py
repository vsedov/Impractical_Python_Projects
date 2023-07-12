"""Turn a word into its Pig Latin equivalent."""

import sys

VOWELS = 'aeiouy'

while True:
    word = input("Type a word and get its pig Latin translation: ")

    pig_Latin = f'{word}way' if word[0] in VOWELS else word[1:] + word[0] + 'ay'
    print()
    print(f"{pig_Latin}", file=sys.stderr)

    try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
    if try_again.lower() == "n":
        sys.exit()
