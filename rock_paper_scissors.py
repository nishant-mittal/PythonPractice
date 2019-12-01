import random
choice = ["rock", "paper", "scissors"]
print("Welcome to the greatest game of all time!")
computer_score = 0
human_score = 0
winning_score = 3
while computer_score < winning_score and human_score < winning_score:
	user_input_player_1 = input("Rock, paper or scissors?: ")
	user_input_player_2 = choice[random.randint(0,2)]
	print("Computer chose " + user_input_player_2)
	if user_input_player_1 == "rock":
		if user_input_player_2 == "rock":
			print("Tie")
		elif user_input_player_2 == "paper":
			print("Computer wins!")
			computer_score += 1
		else:
			print("Human wins!")
			human_score += 1

	elif user_input_player_1 == "paper":
		if user_input_player_2 == "paper":
			print("Tie")
		elif user_input_player_2 == "scissors":
			print("Computer wins!")
			computer_score += 1
		else:
			print("Human wins!")
			human_score += 1

	elif user_input_player_1 == "scissors":
		if user_input_player_2 == "scissors":
			print("Tie")
		elif user_input_player_2 == "rock":
			print("Computer wins!")
			computer_score += 1
		else:
			print("Human wins!")
			human_score += 1

	else:
		print("Something went wrong!")
print(f"Final score: \nComputer: {computer_score} \nHuman: {human_score}")