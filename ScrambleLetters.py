'''
Scramble Letters
Pawelski
3/30/2023
Python II

Instructions:
Start by running the program a few times
to see what it does in general. What does
the program do?

This program is pretty complex! Run the
program in debugging mode so that you can
see how it works step-by-step. When does
the following loop stop repeating?
while len(new_word) < len(word):
    pass

What does this line of code do?
index = random.randint(0, len(word) - 1)

What does this if statement check?
if index not in used_indexes:

What does this code do in the function?
new_word += word[index]
used_indexes.append(index)

What does the variable new_word store in the
scramble() function? What does the list used_indexes
store in the scramble() function? What value is
returned from the function? Where is it returned?
'''

import random

def scramble(word):
    '''
    Scrambles the passed word.
    '''
    new_word = ""
    used_indexes = []
    while len(new_word) < len(word):
        index = random.randint(0, len(word) - 1)
        if index not in used_indexes:
            new_word += word[index]
            used_indexes.append(index)
    return new_word

user_word = input("Enter a word to scramble >> ")
scrambled_word = scramble(user_word)
print(scrambled_word)