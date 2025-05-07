print("Hello and welcome! ")

camper_name = input("Enter your name")

camper_age = 0
while not (5 <= camper_age <= 17):
    try:
        age_input = input("Please enter the camper's age (5-17): ")
        camper_age = int(age_input)
        if not (5 <= camper_age <= 17):
            print("Invalid age. Campers must be between 5 and 17 years old.")
    except ValueError:
        print("Invalid input. Please enter a number for the age.")








