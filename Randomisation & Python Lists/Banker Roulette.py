import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1 Option
random_friends=random.randint(0,4)
print(f"For using randint function: {friends[random_friends]}")

# 2 Option
print(f"For using choice function: {random.choice(friends)}")
