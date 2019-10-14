#date: 14 October 2019
#project: number picker
#description: A number guessing game which will ask the user to guess a number between 1 and 30.

#importing random module
import random

#assigning number range to a variable n, and requesting input from user
n = random.randint(1,30)
guess = int(raw_input("Enter a number from 1 to 30: "))

#program predicts variable n, and outputs result based on user's guess

while n != "guess":
    print
    if guess < n:
        print "Sorry! Your guess is too low. Please try again."
        guess = int(raw_input("Enter a number from 1 to 30: "))
        
    elif guess > n:
        print "Sorry!  Your guess is too high. Please try again."
        guess = int(raw_input("Enter a number from 1 to 30: "))
        
    else:
        print "Great job! You guessed it!"
        break
    print