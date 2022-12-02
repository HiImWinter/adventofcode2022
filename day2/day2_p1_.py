#A = Rock = 1
#B = Paper = 2
#C = scissors 3

#X = rock = 1
#Y = Paper = 2
#Z = scissors = 3

#Your total score is the sum of your scores for each round. 
#The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

#a winning round always adds 6
#a losing round alway adds 0
#a draw always adds 3


fileobj=open("day_2.txt")
lines=fileobj.read().split('\n')
totalScore = 0

rock = 1
paper = 2
scissors = 3

win = 6
tie = 3
lose = 0


for moves in lines:

	print(moves)

	# rock ties with rock

	if(moves == 'A X'):
		print("We have a tie!")
		totalScore += (rock + tie)
		print(rock + tie)

	# rock loses to paper

	elif(moves == 'A Y'):
		print("Player wins!")
		totalScore += (paper + win)
		print(paper+win)

	# rock beats scissors

	elif (moves == 'A Z'):
		print("Player loses!")
		totalScore += (scissors + lose)
		print(scissors + lose)

	# paper beats rock

	elif(moves == 'B X'):
		print("Player loses!")
		totalScore += (rock + lose)
		print(rock + lose)

	# paper ties with paper

	elif(moves == 'B Y'):
		print("We have a tie!")
		totalScore += (paper + tie)
		print(paper + tie)

	# paper loses to scissors

	elif(moves == 'B Z'):
		print("Player wins!")
		totalScore += (scissors+win)
		print(scissors+win)


	#scissors lose to rock

	elif(moves == 'C X'):
		print("Player wins!")
		totalScore += (rock + win)
		print(rock + win)

	# scissors beat paper

	elif(moves == 'C Y'):
		print("Player loses!")
		totalScore += (paper + lose)
		print(paper + lose)


	# scissors tie with scissors

	elif(moves == 'C Z'):
		print("We have a tie!")
		totalScore += (scissors+tie)
		print(scissors+tie)

	else:
		print("We decided we're validating input and this is not a valid rock paper scissors input for this program so yeah")


print(totalScore)
