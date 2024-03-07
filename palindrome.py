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
