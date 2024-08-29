# Create a number guessing game where the computer randomly selects a number between 1 and 100, 
# and the user has to guess what it is. The user gets up to 10 attempts to guess the number. 

import random
def number_guessing():
    number_to_guess = random.randint(1,100)
    print("Number between 1 to 100")

    for attempt in range(1,11):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}"))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Introduce number between 1 to 100")
            except ValueError:
                print("Invalid Input")

        if guess < number_guessing: print("Too low")
        elif guess > number_to_guess: print("Too high")
        else:
          print("You guessed the number {guess}")
          return
        
    print("You used all the attemps, the number was {number_to_guess}")

number_guessing()
          