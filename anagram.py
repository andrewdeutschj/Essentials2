text1 = input("Enter some text: ")
text2 = input("Enter more text: ")

text1x = text1.replace(" ", "")
text2x = text2.replace(" ", "")

if ( len(text1) > 0 and len(text2) > 0 ) and ( sorted(text1x.upper()) == sorted(text2x.upper()) ):
    print("Anagrams")
else:
    print("Not anagrams")