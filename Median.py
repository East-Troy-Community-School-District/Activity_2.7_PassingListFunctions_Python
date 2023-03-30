'''
Median
Pawelski
3/30/2023
Python II

Instructions:
Read the code and run the program to see what it
does. You may even want to run the program in
debugging mode and step through the program
line-by-line. What is the median? What is the mode?

What would happen if we changed the while loop that
populates the list so that it looks like this...
number = 0
while number != -1:
    number = input("Enter a number (-1 to stop) >> ")
    user_numbers.append(number)

What does the // operator calculate? Again, what
the benefit of using a function in this program?
'''

def median(numbers):
    '''
    Returns the median of the numbers in the list.
    '''
    numbers.sort()
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2
    return numbers[middle_index]


user_numbers = []
number = input("Enter a number (-1 to stop) >> ")
while number != -1:
    user_numbers.append(number)
    number = input("Enter a number (-1 to stop) >> ")

print("Median:", median(user_numbers))
