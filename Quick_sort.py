import random

num_numbers = 1000
min_value = 1
max_value = 1000
random_numbers = []

for i in range(num_numbers):
    random_number = random.randint(min_value, max_value)
    random_numbers.append(random_number)

print(random_numbers)
