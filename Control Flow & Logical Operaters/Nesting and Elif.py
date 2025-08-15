print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age=int(input("Enter Your Age: "))
    if (age > 15) & (age <= 20):
        print("Your ticket Price is Rs: 50.")
    elif (age > 20) & (age <=25):
        print("Your ticket Price is Rs: 75.")
    elif age > 25:
        print("Your ticket Price is Rs: 100.")
    else:
        print("Children are Not Allow.")
else:
    print("Sorry you have to grow taller before you can ride.")
