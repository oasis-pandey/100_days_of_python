import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0,4)
friend_paying_bill = friends[random_number]
print(f"The person who is paying the bill is: {friend_paying_bill}")