import sys
from random import randint
number = randint(1, 10)
print(number)

while True:
	number_guessed = int(input("Guess a number between 1 and 10: "))
	if number_guessed > number:
		print("Too high! try again!")
	elif number_guessed < number:
		print("Too low! try again")
	else:
		print("You guesses it!You won!")
		choice = input("Do you want to continue? (y/n): ")
		if choice == "y":
			number = randint(1, 10)
			number_guessed = None
		else:
			print("Thanks for playing!")
			break
			
		






