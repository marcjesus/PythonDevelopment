#Example of Shallow Copy
import copy

original_list = [1, [2, 3], 4]
shallow_copy_list = original_list.copy()

# Modifying the shallow copy
shallow_copy_list[1][0] = 99

# Changes are reflected in the original list as well
print("Original List:", original_list)  
# Output: [1, [99, 3], 4]
print("Shallow Copy List:", shallow_copy_list)  
# Output: [1, [99, 3], 4]
