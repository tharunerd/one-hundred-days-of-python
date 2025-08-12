# # bmi calculatot
# ###
# height_cm = float(input("Enter your height in centimeters: "))
# height_m = height_cm / 100
# weight = float(input("Enter your weight in kilograms: "))   
# bmi = weight / (height_m ** 2)
# print(f"Your BMI is: {bmi:.2f}")
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("You have a normal weight.")
# elif 25 <= bmi < 29.9:
#     print("You are overweight.")
# elif 30 <= bmi < 34.9:
#     print("You have obesity (Class 1).")
# elif 35 <= bmi < 39.9:
#     print("You have obesity (Class 2).")
# else:
#     print("You have severe obesity (Class 3).")

# */

# bmi using error handling 

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    print("Welcome to the BMI Calculator!")

    while True:
        try:
            weight = float(input("Enter your weight in kilograms (e.g., 70.5): "))
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")

            height = float(input("Enter your height in meters (e.g., 1.75): "))
            if height <= 0:
                raise ValueError("Height must be a positive number.")

            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                print("You are underweight.")
            elif 18.5 <= bmi < 25:
                print("You have a normal weight.")
            elif 25 <= bmi < 30:
                print("You are overweight.")
            else:
                print("You are obese.")
            
            break  # Valid input, exit loop

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")

        finally:
            print("Thank you for using the BMI calculator.\n")

if __name__ == "__main__":
    main()
