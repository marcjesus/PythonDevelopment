# The map() function takes each element from the iterable, applies the specified function to it, 
# and returns an iterator containing the results of applying the function to each element.

Numbers = [1,2,3,4]
squared_numbers = list(map(lambda x: x ** 2, Numbers))
print(squared_numbers)  #OUTPUT : [1, 4, 9, 16]
