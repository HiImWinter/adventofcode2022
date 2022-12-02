
# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, 
#Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. 
#The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.


fileobj=open("day_2.txt")
lines=fileobj.read().split('\n')
totalScore = 0

rock = 1
paper = 2
scissors = 3

win = 6
tie = 3
lose = 0

#X = lose
#Y = draw
#Z = win



for moves in lines:

	print('\n'+moves)


#rock conditions -- 

	#computer played rock and this needs to end in a loss for the player
	#rock beats scissors
	if(moves == 'A X'):
		print("Computer played rock, User played scissors, user loses!")
		totalScore += (scissors + lose)
		print("points earned for this round:", rock + lose)

	#computer played rock and this needs to end in a draw
	#rock ties with rock
	elif(moves == 'A Y'):
		print("Computer played rock, User played rock, we have a tie! ")
		totalScore += (rock + tie)
		print("points earned for this round:",rock+tie)


	#computer played rock and this needs to end in a win for the player
	# rock loses to paper
	elif (moves == 'A Z'):
		print("Computer played rock, User played paper, user wins!")
		totalScore += (paper + win)
		print("points earned for this round:",paper + win)


#paper conditions -- 

	#computer played paper and this needs to end in a loss for the player
	#paper beats rock
	elif(moves == 'B X'):
		print("Computer played paper, User played rock, user loses!")
		totalScore += (rock + lose)
		print("points earned for this round:",rock + lose)


	#computer played rock and this needs to end in a draw
	#paper ties with paper
	elif(moves == 'B Y'):
		print("Computer played paper, User played paper, we have a tie!")
		totalScore += (paper + tie)
		print("points earned for this round:",paper + tie)

	#computer played paper and this needs to end in a win for the player
	#paper loses to scissors
	elif(moves == 'B Z'):
		print("Computer played paper, User played scissors, user wins!")
		totalScore += (scissors+win)
		print("points earned for this round:",scissors+win)


#scissor conditions --

	#computer played scissors and this needs to end in a loss for the player
	#scissors beats paper
	elif(moves == 'C X'):
		print("Computer played scissors, User played paper, user loses!")
		totalScore += (paper + lose)
		print("points earned for this round:",paper + lose)

	#computer played scissors and this needs to end in a draw
	#scissors ties with scissors
	elif(moves == 'C Y'):
		print("Computer played scissors, User played scissors, we have a tie!")
		totalScore += (scissors + tie)
		print("points earned for this round:",scissors + tie)


	# computer played scissors and this needs to end in a win for the player
	# scissors loses to rock
	elif(moves == 'C Z'):
		print("Computer played scissors, User played rock, user wins!")
		totalScore += (rock+win)
		print("points earned for this round:",rock+win)

	else:
		print("We decided we're validating input and this is not a valid rock paper scissors input for this program so yeah")


print("Player's Total Score:", totalScore)
