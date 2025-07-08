# Band Name Generator

# This simple Python program helps you come up with a fun band name!
# It asks you for the name of the city you grew up in and your pet’s name,
# then combines them to suggest a unique band name. 
# It’s a beginner-friendly project to practice taking user input
#  and displaying output in Python.


print("welcome to the band name generator")
city = input("which city did you grow up in?\n")
# print(city)
pet = input("what is your pet name?\n")
# print(pet)

print("your band name could be {} {}".format(city, pet))
