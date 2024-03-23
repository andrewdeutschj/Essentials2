"""
Some say that the Digit of Life is a digit evaluated using somebody's birthday.
It's simple – you just need to sum all the digits of the date. If the result contains more than one digit,
you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.

Test your code using the data we've provided.

Test input: 19991229
    result: 6
Test input: 20000101
    result: 4
"""

def calc_num(string_arg):
    total = 0
    for i in (string_arg):
        total += int(i)
    return total

bday = input("Enter your birthdate in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY: ")
if bday.isdigit() and len(bday) == 8:
    sum_strng = calc_num(bday)
    while len(str(sum_strng)) > 1:
        sum_strng = calc_num(str(sum_strng))
    print("Digit of life: ", sum_strng)
else:
    print("BAD date!!")


