# PRACTICAL NO. 10
# AIM: Program to read a line of text and count letters and words

text = input("Enter a line of text: ")
letters = sum(c.isalpha() for c in text)
words = len(text.split())
print("Number of letters:", letters)
print("Number of words:", words)
