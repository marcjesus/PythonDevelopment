def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

numerator = input("Introduce numerator: ")
denominator = input("Introduce denominator: ")

result = divide(int(numerator), int(denominator))
print("Result of division:", result)


#The ‘assert’ statement checks if the ‘denominator’ is not zero before performing the division. 
#If the ‘denominator’ is zero, the program raises an ‘AssertionError’