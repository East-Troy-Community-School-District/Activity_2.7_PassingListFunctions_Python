'''
Mail List
Pawelski
3/30/2023
Python II

Instructions:
Read the code and run the program to see what it
does. You may even want to run the program in
debugging mode and step through the program
line-by-line. Why must we use a for loop with
indexes?
'''

names = []
addresses = []
cities = []
states = []
zip_codes = []

repeat = "y"
while repeat == "y":
    name = input("Enter a name >> ")
    address = input("Enter their address >> ")
    city = input("Enter their city >> ")
    state = input("Enter their state >> ")
    zip_code = input("Enter their zip >> ")
    names.append(name)
    addresses.append(address)
    cities.append(city)
    states.append(state)
    zip_codes.append(zip_code)
    repeat = input("Do you need to enter another person? (y/n) >> ")
    print()

print("Here is your mailing list...")
for i in range(0, len(names)):
    print(names[i])
    print(addresses[i])
    print(cities[i], states[i], zip_codes[i], sep=", ")
    print()