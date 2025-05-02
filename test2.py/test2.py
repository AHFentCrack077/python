print ("hello")
Name = input ("What is your name: ")
age = input ("What is your age: ")
age = int(age)
program_choice = ["1. Cultural immersion", "2. Kayaking and pancakes", "3. Mountain biking"]
if age > 17:
    print("You cant go becouse you are to old.")
elif 5 <= age <= 17:
    print("You can go.")
else:
    print("you must be at least 5 years old to go.")

print('choose an activity:')
print(f'{program_choice[0]}')
print(f'{program_choice[1]}')
print(f'{program_choice[2]}')
activity = input("enter the number of your choosen activity: ")



