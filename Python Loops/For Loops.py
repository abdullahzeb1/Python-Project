import random
fruits = ["Apple", "Peach", "Banana"]
fruits_name=random.randint(0,2)
for fruit in fruits:
    print("printing for Loop: ("+ fruit + ")")
    print("printing for Loop with random.choice: (" + fruit + f" + Mango + {random.choice(fruits)})")
    print("printing with ramdom.randint: (" + fruits[fruits_name]+")")
