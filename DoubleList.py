'''
Double List
Pawelski
3/30/2023
Python II

Instructions:
Before running the program, predict what it
will display in the console. Check your
prediction by running the program. Why were
the values in numbers doubled?
'''

def double(num_list):
    '''
    Doubles the values in num_list.
    '''
    for i in range(0, len(num_list)):
        num_list[i] *= 2

numbers = [4, 1, 8, 3, 9, 1, 11, 17, 35, 99, 2]
double(numbers)
print(numbers)