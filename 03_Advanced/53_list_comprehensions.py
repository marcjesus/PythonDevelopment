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

# Challenge 5 : Create a function which princts the second lowest score from a list

def print_lowest_scores(nested_list):
    if not nested_list:
        print("The list is empty.")
        return

    # Find the lowest score
    lowest_score = min(item[1] for item in nested_list)

    # Find names associated with the lowest score
    lowest_score_names = [item[0] for item in nested_list if item[1] == lowest_score]

    print("Names with the lowest score(s):", lowest_score_names)

# Example usage:
scores_list = [["Alice", 85], ["Bob", 70], ["Charlie", 90], ["Dave", 70], ["Eve", 80]]
print_lowest_scores(scores_list)
