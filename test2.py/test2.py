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

camp_options = {
    "1": {"name": "Cultural immersion", "days": 5, "difficulty": "easy", "cost": 800},
    "2": {"name": "Kayaking and pancakes", "days": 3, "difficulty": "moderate", "cost": 400},
    "3": {"name": "Mountain biking", "days": 4, "difficulty": "difficult", "cost": 900}
}

print("\nAvailable Camp Options:")
for key, camp in camp_options.items():
    print(f"{key}. {camp['name']} - {camp['days']} days, {camp['difficulty']}, ${camp['cost']}") 

chosen_camp_key = ""
while chosen_camp_key not in camp_options:
    chosen_camp_key = input("Enter the number of your chosen activity (1, 2, or 3): ")
    if chosen_camp_key not in camp_options:
        print("Invalid choice. Please enter 1, 2, or 3.")

chosen_camp = camp_options[chosen_camp_key]

print(f"\nYou have chosen: {chosen_camp['name']}")
print(f"Details: {chosen_camp['days']} days, Difficulty: {chosen_camp['difficulty']}")

meal_choice = input("Please enter your meal preference (e.g., standard, vegetarian, vegan): ")
transport_needed = ""
while transport_needed.lower() not in ['yes', 'no']:
    transport_needed = ()
    transport_needed = input("Will you need transport? (yes/no): ")
    if transport_needed.lower() not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")

Transport_cost = 80
Transport = input("yes or no")
if Transport.lower() == "yes":
    print("")
    transport_fee = Transport_cost
elif Transport.lower() == "no":
    print("")
    transport_fee = 0
else:
 confirm_attendance = ""
while confirm_attendance.lower() not in ['yes', 'no']:
    confirm_attendance = input("Are you attending this camp? (yes/no): ")
    if confirm_attendance.lower() not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")




