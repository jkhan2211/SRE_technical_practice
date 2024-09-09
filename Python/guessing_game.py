# Task 1: Python uses
# completed

import random


# Task 5: Python Functions
def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        # Divide and counquer approach
        guess = lowval + (highval - lowval) // 2
        if guess == randnum:
            return count

        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess - 1, randnum, count)
        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randnum, count)

    else:
        return -1


# End of function


randNum = random.randint(1, 101)
print(randNum)

count = 0
guess = -99

# Task 4: Python Looping
while guess != randNum:
    guess = (int)(input("Please enter a number between 1 and 100: "))
    # Task 2: Python Variables and Input
    # Guess the user input:
    # Task 3: Python Decision Constructs
    if guess < randNum:
        print("higher!")
    elif guess > randNum:
        print("lower!")
    else:
        print("You guessed it!!")
        break
    count = count + 1

# end of while loop
print("You took " + str(count) + " steps to guess the number")
print(
    "Computer took "
    + str(computerGuess(0, 100, randNum))
    + " steps to guess the number"
)
