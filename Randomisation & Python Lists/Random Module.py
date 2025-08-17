import random
random_number=random.random()
print(random_number)
print(random_number*10)

random_float=random.uniform(1,5)
print(random_float)

random_integer=random.randint(10,20)
print(random_integer)

if random_integer % 2 == 0:
    print("Heads")
else:
    print("Tails")

random_triangular=random.triangular(2, 10, 6)
print(random_triangular)