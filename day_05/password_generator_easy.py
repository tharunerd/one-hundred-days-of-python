# random password generator easy level
# This code generates a random password based on user input for the number of letters, numbers,
import random   

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

user_letters = int(input("Enter the number of letters in your password: "))
user_numbers = int(input("Enter the number of numbers in your password: "))
user_symbols = int(input("Enter the number of symbols in your password: "))

#Eazy Level
password = ""

for char in range(1, user_letters + 1):
  password += random.choice(letters)
for char in range(1, user_symbols + 1):
  password += random.choice(symbols)
for char in range(1, user_numbers + 1):
  password += random.choice(numbers)
print("password = ", password)