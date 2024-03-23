"""
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent
Test your code using the data we've provided.

Test input:
    Listen
    Silent
    *result: Anagrams
Test input:
    modern
    norman
    *result: Not anagrams
"""

text1 = input("Enter some text: ")
text2 = input("Enter more text: ")

text1x = text1.replace(" ", "")
text2x = text2.replace(" ", "")

if ( len(text1) > 0 and len(text2) > 0 ) and ( sorted(text1x.upper()) == sorted(text2x.upper()) ):
    print("Anagrams")
else:
    print("Not anagrams")