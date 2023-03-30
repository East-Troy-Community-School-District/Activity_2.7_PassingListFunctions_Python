'''
Tilda Border
Pawelski
3/30/2023
Python II

Instructions:
Before running the program, predict what it
will display in the console. Check your prediction
by running the program. How many parameters
does the display_border() function have? How
many arguments must be passed to the display_border()
function? Consider the following call...
display_border("!", 200)

Which parameter gets "!"? Which parameter gets 200?

Modify the program by adding another call to the
display_border() function to print a border
consisting of 100 "<>"s. Hint: There will be a
total of 200 characters in the border.
'''

def display_border(symbol, amount):
    '''
    Displays a border using the passed symbol. Repeats symbol the passed
    amount of times. Automatically goes to next line.
    '''
    for i in range(0, amount):
        print(symbol, end="")
    print()

display_border("~", 50)
display_border("-", 25)
