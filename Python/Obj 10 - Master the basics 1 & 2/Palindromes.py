import re

text = input("Enter text:")


def is_palindrome(text):
    # Lower case
    text = text.lower()
    # Remove non-alphanumeric characters
    text = re.sub(r"\W+", "", text)

    reversedText = text[::-1]

    return reversedText == text


if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
