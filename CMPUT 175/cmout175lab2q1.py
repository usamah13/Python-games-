
from random import randint

#ACCEPTED_INPUTS = [1,5,10,25]
#BREAK_LOOP = "ERROR"

def generate_target_value():
	return (randint(1, 99))

def ingest_user_value(goalInt, var):
	ACCEPTED_INPUTS = [1,5,10,25]
	if var.isdigit() and int(var) in ACCEPTED_INPUTS:
		inputValue = int(var)
		goalInt -= inputValue
		return (goalInt, inputValue)
	elif var.strip() == "":
		return (False, False)
	else:
		print("Invalid entry - Try again!")
		return (goalInt, 0)

def main():
	
	quit = False
	while (quit is False):

		goalInt = str(generate_target_value())
		originalGoal = goalInt
		totalValue = 0

		print("Game Session Starts")
		print("Enter coins values as 1-penny, 5-nickel, 10-dime, and 25-quarter.")
		print("Enter coins that add up to " + goalInt + " cents, one per line.")

		goalInt = int(goalInt)
		while (goalInt != 0):
			var = input("Enter a valid coin value > ")
			outcome = ingest_user_value(goalInt, var)
			if outcome[0] < 0:
				print("Game Session Ends")
				print("Here is the outcome :")
				totalValue += outcome[1]
				print ("Failure ‐ you entered " + str(totalValue) + " cents")
				delta = (int(originalGoal) - totalValue) * -1
				print("The amount exceeds " + str(originalGoal) + " cents by " + str(delta) + " cents")
				goalInt = 0
			elif outcome[0] is False:
				print("Session Ends!")
				print("Game Session Ends")
				print("Here is the outcome :")
				totalValue += outcome[1]
				print ("Failure ‐ you only entered " + str(totalValue) + " cents")
				delta = (int(originalGoal) - totalValue)
				print("You are short of " + str(delta) + " cents")
				goalInt = 0
			elif outcome[0] == 0:
				print("Game Session Ends")
				print("Here is the outcome :")
				print("Success!")
				goalInt = 0
			else:
				goalInt = outcome[0]
				totalValue += outcome[1]

		userend = input("Play another game session (y/n)? ")
		if userend == "n":
			print("Thanks for playing ... goodbye")
			quit = True
		else:
			quit = False

main()