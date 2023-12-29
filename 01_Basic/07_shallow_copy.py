# A shallow copy creates a new compound object and then adds a reference to the object found in the original, 
# as a result, if the elements inside the original object are mutable, changes made to these elements will affect both 
# the original object and the shallow copy. A deep copy creates a new object and creates a new copy of objects whose changes made 
# to the objects inside the deep copy do not affect the original object, and vice versa. 


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
