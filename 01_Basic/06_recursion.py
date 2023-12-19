def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive step: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
result = factorial(5)  

# Calculates 5! = 5 * 4 * 3 * 2 * 1 = 120
print("Factorial:", result)  
# Output: Factorial: 120
