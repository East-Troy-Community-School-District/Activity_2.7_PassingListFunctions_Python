'''
Count Name
Pawelski
3/30/2023
Python II

Instructions:
Read the code and run the program to see what it
does. You may even want to run the program in
debugging mode and step through the program
line-by-line. How is a list passed to a function?
How did we populate the list? What is "zzzzz"?

Let's modify the code a bit. Instead of having
the program ask the user for the name to count,
let's have the program report the number of times
each name in the list appears. We will make it so
that the program does not repeat any of the names
when reporting the statistics.

What is the benefit of using a function in this
program?
'''

def count_name(names_list, name_to_count):
    '''
    Returns the number of times the name appears in the list.
    '''
    count = 0
    for name in names:
        if name == name_to_count:
            count += 1
    return count


names = []
name = input("Enter a name (zzzzz to stop) >> ")
while name != "zzzzz":
    names.append(name)
    name = input("Enter a name (zzzzz to stop) >> ")
    
name = input("Enter a name to count >> ")
print("The name", name, "appears", count_name(names, name), "times.")
