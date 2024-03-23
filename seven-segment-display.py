"""
You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) – that's how we imagine it:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # #
  # ### ### ### ### ###   # ### ### # #
  # #     #   #   # # #   # # #   # # #
  # ### ###   # ### ###   # ### ### ###
Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.
"""

number_lines = \
{
    1: {1: [' ',' ','#'], 2: ['#','#','#'], 3: ['#','#','#'], 4: ['#',' ','#'], 5: ['#','#','#'],
        6: ['#','#','#'], 7: ['#','#','#'], 8: ['#','#','#'], 9: ['#','#','#'], 0: ['#','#','#'] },
    2: {1: [' ',' ','#'], 2: [' ',' ','#'], 3: [' ',' ','#'], 4: ['#',' ','#'], 5: ['#',' ',' '],
        6: ['#',' ',' '], 7: [' ',' ','#'], 8: ['#',' ','#'], 9: ['#',' ','#'], 0: ['#',' ','#'] },
    3: {1: [' ',' ','#'], 2: ['#','#','#'], 3: ['#','#','#'], 4: ['#','#','#'], 5: ['#','#','#'],
        6: ['#','#','#'], 7: [' ',' ','#'], 8: ['#','#','#'], 9: ['#','#','#'], 0: ['#',' ','#'] },
    4: {1: [' ',' ','#'], 2: ['#',' ',' '], 3: [' ',' ','#'], 4: [' ',' ','#'], 5: [' ',' ','#'],
        6: ['#',' ','#'], 7: [' ',' ','#'], 8: ['#',' ','#'], 9: [' ',' ','#'], 0: ['#',' ','#'] },
    5: {1: [' ',' ','#'], 2: ['#','#','#'], 3: ['#','#','#'], 4: [' ',' ','#'], 5: ['#','#','#'],
        6: ['#','#','#'], 7: [' ',' ','#'], 8: ['#','#','#'], 9: ['#','#','#'], 0: ['#','#','#'] }
}

user_input = int(input("Enter an integer number: "))

for row in (sorted(number_lines.keys())):
    #for each number given
    for num_given in (str(user_input)):
        my_number = int(num_given)
        for col in range(len(number_lines[row][my_number])):
            print(number_lines[row][my_number][col], end=' ')
        print(' ', end=' ')
    print()