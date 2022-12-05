#Some of the pairs have noticed that one of their assignments fully contains the other. 
#For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, 
#one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. 
#In this example, there are 2 such pairs.

#In how many assignment pairs does one range fully contain the other?


fileobj=open("day_4.txt")
allPairs=fileobj.read().split('\n')
overlaps_pt1 = 0
overlaps_pt2 = 0



for currentPair in allPairs:

	splitPair = currentPair.split(',')
	
	firstRange = splitPair[0]

	secondRange = splitPair[1]


	newFirstRange = firstRange.split('-')
	print("This is my first range: ",newFirstRange)
	newSecondRange = secondRange.split('-')
	print("This is my second range: ",newSecondRange)

	newSetFirst = set(range(int(newFirstRange[0]),int(newFirstRange[1])+1))
	newSetSecond = set(range(int(newSecondRange[0]),int(newSecondRange[1])+1))
	
	pairIntersection = newSetFirst.intersection(newSetSecond)

	# for part 2, checking to see if there is any partial overlaps
	# if the intersection returns a value, it confirms overlap

	if pairIntersection:
		overlaps_pt2 += 1

	print("This is my first set: ",newSetFirst)
	print("This is my second set: ",newSetSecond)
	print("This is my intersection:", pairIntersection)
	
	if (newSetFirst == pairIntersection or newSetSecond == pairIntersection):

		print("There's an overlap!")
		overlaps_pt1 += 1

	else:

		print("No overlap!")

	print('\n')


print("Total overlaps:", overlaps_pt1)
print("Total partial overlaps",overlaps_pt2)

		

#print(allPairs)

