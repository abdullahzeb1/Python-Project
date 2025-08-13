print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $:"))
tip = int(input("What percentage tip would you like to give? 10 12 15 = "))
people = int(input("How many people to split the bill? "))

print(f"Bill Amount is: {bill}")
tip_percentage= tip/100
total_tip=bill*tip_percentage
print(f"Total Tip Amount: {total_tip} ")
total_bill=bill+total_tip
print(f"Total Bill Amount: {total_bill}")
peoples= (total_bill/people)
peoples_bill=round(peoples,2)
print(f"Every Person Bill Pay: {peoples_bill}")


