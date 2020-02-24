#!/usr/bin/env
# Description: This is a simple calculator program. The user should be able to select from 4 different options: add, subtract, multiply, or divide.

import sys

def add (x,y):
	return x + y

def subtract (x,y):
	return x - y

def multiply (x,y):
	return x * y

def divide (x, y):
	return x / y


print ("Please select an option from below: \n" \
	"1. Add\n" \
	"2. Subtract\n" \
	"3. Multiply\n" \
	"4. Divide\n")

#User input for options
choice = input ("Choose an option by typing the operation itself, or a number 1-4: ")

options = ["Add", "Subtract", "Multiply", "Divide"]
options_num = ["1","2","3","4"]

if choice in options or options_num:
	pass
else:
	print ("Sorry. That's not an option")
	sys.exit(0)

#User input for numbers
num1 = int(input("Enter the the first number: "))
num2 = int(input("Enter the second number: "))


#Where the magic happens
if '1' in choice or 'Add' in choice:
	print ("Let me add that for you....")
	print (num1, "+", num2, "=", 
		add(num1, num2))

elif '2' in choice or 'Subtract' in choice:
	print ("Let me subtract that for you....")
	print (num1, "-", num2, "=",
		subtract(num1, num2))

elif '3' in choice == '3' or 'Multiply' in choice:
	print ("Let me multiply that for you....")
	print (num1, "*", num2, "=",
		multiply(num1, num2))

elif '4' in choice or 'Divide' in choice:
	print ("Let me divide that for you....")
	print (num1, "/", num2, "=",
		divide(num1, num2))
