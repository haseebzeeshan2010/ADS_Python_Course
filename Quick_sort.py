import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = []
    middle = []
    right = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return quicksort(left) + middle + quicksort(right)

# Example usage:

num_numbers = 1000
min_value = 1
max_value = 1000
random_numbers = []


for i in range(num_numbers):
    random_number = random.randint(min_value, max_value)
    random_numbers.append(random_number)

print(random_numbers)
print()
sorted_array = quicksort(random_numbers)
print(sorted_array)
