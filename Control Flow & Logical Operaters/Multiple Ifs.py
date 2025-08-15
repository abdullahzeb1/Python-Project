print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm: "))
bill=0

if height >= 120:
    print("You can ride the rollercoaster.")
    age=int(input("Enter Your Age: "))

    if (age > 15) & (age <= 20):
        bill=50
        print("You ara Pay Rs: 50.")
    elif (age > 20) & (age <=25):
        bill=75
        print("You are Pay Rs: 75.")
    elif age > 25:
        bill=100
        print("You are Pay Rs: 100.")
    else:
        print("Children are Not Allow.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo=="y" or wants_photo=="Y":
        bill+=20
        print(f"Your Bill is {bill}")
    else:
        print(f"Your Bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
