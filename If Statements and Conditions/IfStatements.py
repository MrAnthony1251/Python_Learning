# if = stands for doing somenting if the condition is true
# else = Do Somenting Else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to enter in the military")
elif age >= 18:
    print("You are now signed up for the military now it's time to become a marine")
elif age < 0:
    print("you haven't born yet but i admire your devotion to enter in the military")
else: 
    print("You must be 18+ to entry in the military!")


## Second Lesson ##

response = input("Would you like food (Y/N): ")

if response == "Y":
    print("Have Some food!")
else:
    print("No food is available")


## Third Lesson ##

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello{name}")