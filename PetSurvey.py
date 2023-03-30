'''
Pet Survey
Pawelski
3/30/2023
Python II

Instructions:
What does this program do?
'''

def conduct_survey(prompt):
  '''
  Gathers all the information by conducting the survey.
  Returns a list of the survey results.
  '''
  pets = []
  pet = input(prompt + " >> ")
  while pet != "zzzzz":
    pets.append(pet)
    pet = input(prompt + " (zzzzz to quit) >> ")
  return pets


pets = conduct_survey("Enter the type of pet you have")
print()
print("Here are the results of the survey:")
print(pets)
