# # # # variable = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# # # #
# # # # # thirdvalue = variable["key3"]
# # # # # print(thirdvalue)
# # # # # print( "key3" in variable)
# # # # # print("88" not in variable)
# # # # # print (variable)
# # # # # print(variable.keys())
# # # # # value = (variable.values())
# # # # # print(variable.items())
# # # # print (len(variable))
# # # # # for keys in variable:
# # # # #     print(keys)
# # # # # for values in variable.values():
# # # # #     print (values)
# # # #
# # # # for key , value in variable.items():
# # # #     print(key, value)
# # # #
# # # # print(variable.get("Michael Jackson", "That is not a key that appears in the dictionary."))
# # # # Step 1: Create a dictionary with consonants as keys and 'consonant' as value
# # # alphabet = 'abcdefghijklmnopqrstuvwxyz'
# # # consonants = 'bcdfghjklmnpqrstvwxyz'
# # # consonant_dict = dict.fromkeys(consonants, 'consonant')
# # #
# # # # Step 2: Use a for loop and the .items() method to print key-value pairs
# # # for key, value in consonant_dict.items():
# # #     print(f"{key} {value}")
# # #
# # # # Step 3: Define the fast_food_items dictionary
# # # fast_food_items = {
# # #     "McDonald's": "Big Mac",
# # #     "Burger King": "Whopper",
# # #     "Chick-fil-A": "Original Chicken Sandwich"
# # # }
# # #
# # # # Step 4: Pop and print "Big Mac"
# # # big_mac = fast_food_items.pop("McDonald's")
# # # print(f"Popped item: McDonald's - {big_mac}")
# # #
# # # # Step 5: Use .popitem() to remove the last key-value pair
# # # removed_item = fast_food_items.popitem()
# # # print(f"Removed item using popitem: {removed_item}")
# # #
# # # # Step 6: Print the updated fast_food_items dictionary
# # # print("Updated fast_food_items dictionary:", fast_food_items)
# # for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
# #     print(key, value)
# #
# # fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# # print(fast_food_items.pop("McDonald's"))
# #
# # fast_food_items.popitem()
# # print(fast_food_items)
#
# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# internet_celebrities.update(another_one)  # 2
# gamers = internet_celebrities.copy()  # 3
# internet_celebrities.clear()  # 4
# print(internet_celebrities)  # 5
# print(gamers)  #
#
# empty = dict ()
# print (type(empty))
#

dictt = {1:"2",2:1 }
print(dictt)

# tup = (1,2,3,4,5,(2,4,6,8,0,1))
# c=  (1 in tup)
# print (type (c))