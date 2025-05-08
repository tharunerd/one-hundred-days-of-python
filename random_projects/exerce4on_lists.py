# arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# print(arctic_animals)
# # del arctic_animals
# arctic_animals.remove("elephant")
# print(arctic_animals)
# arctic_animals.insert(2, "snowy owl")
# print(arctic_animals)
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())