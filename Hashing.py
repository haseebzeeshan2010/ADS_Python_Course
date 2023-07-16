# Create an empty hash map
hash_map = {}

# Add key-value pairs to the hash map
hash_map["apple"] = 1
hash_map["banana"] = 2
hash_map["cherry"] = 3

# Access values using keys
print(hash_map["apple"])  # Output: 1
print(hash_map["banana"])  # Output: 2

# Update values
hash_map["apple"] = 5
print(hash_map["apple"])  # Output: 5

# Remove a key-value pair
del hash_map["cherry"]
print(hash_map)  # Output: {'apple': 5, 'banana': 2}