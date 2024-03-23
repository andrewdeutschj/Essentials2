"""
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent;
there are more than a few correct solutions – try to find more than one.
Test your code using the data we've provided.

Test input: Ten animals I slam in a net
    result: It's a palindrome
Test input: Eleven animals I slam in a net
    result: It's not a palindrome
"""


text = input("Enter some text: ")
textnospace = text.replace(" ", "")

tlen = len(textnospace)
halflen = tlen // 2
first_half = textnospace[0:halflen]
second_half = textnospace[tlen:halflen:-1]

if first_half.upper() == second_half.upper():
    print("It's a palindrome")
else:
    print("Not a palindrome")
