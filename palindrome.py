import sys

text = sys.argv[1]

if text.lower() == text.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


    