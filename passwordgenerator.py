#importing random module

import random

#storing every letter in the alphabet and every number in the char variable

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

#assigning users input to number, and coverting that number into an integer

number = input('How many passwords should I generate for you?')
number = int(number)

#assigning users input to length, and coverting that number into an integer

length = input('How long do you want your password to be?')
length = int(length)

#printing out password

print('\nHere are your passwords:')

#storing randomly chosen characters in password variable and printing out the variable. The password length will be whatever the user declares.

for pwd in range(number):
    password = ''
    for c in range(length):

#the =+ signs ensure that different characters are chosen each time within the span of the # attached to the length variable.

        password += random.choice(chars)
    print(password)

