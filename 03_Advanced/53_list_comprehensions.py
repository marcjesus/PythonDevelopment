# Challenge 1 : Generate a list of squares of numbers from 1 to 5
squares = [ x**2 for x in range(5)]
print(f"Output for challenge 1 {squares}")

# Challenge 2 : Filter a list which includes only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [ x for x in range(numbers) if x%2 ==0 ]


# Challenge 3  : Create a list of tuples containing the numbers and their sequences
numbers = [1, 2, 3, 4, 5]

# Challenge 4 : Create a list with three coordinates where in doesn't print if n is the sum of the coordinates
x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
constrain = x + y + z
coordinates = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(coordinates)
