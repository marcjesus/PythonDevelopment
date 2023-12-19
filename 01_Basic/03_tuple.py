# Creating a tuple
my_tuple = (1, 2, 3, "hello", 4.5)


# Accessing elements in a tuple
print("Tuple elements:")
print("First element:", my_tuple[0])  # Output: 1
print("Third element:", my_tuple[2])  # Output: 3
print("Fifth element:", my_tuple[4])  # Output: 4.

# Tuple slicing
subset_tuple = my_tuple[1:4]
print("Subset tuple:", subset_tuple)  # Output: (2, 3, 'hello')


# Nested tuple
nested_tuple = (1, (2, 3), ("hello", "world"))
print("Nested tuple:", nested_tuple)  # Output: (1, (2, 3), ('hello', 'world'))
