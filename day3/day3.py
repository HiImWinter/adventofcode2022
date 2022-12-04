#for when you forget about ASCII values

priority_dictionary = {
	
'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26,
'A':27,
'B':28,
'C':29,
'D':30,
'E':31,
'F':32,
'G':33,
'H':34,
'I':35,
'J':36,
'K':37,
'L':38,
'M':39,
'N':40,
'O':41,
'P':42,
'Q':43,
'R':44,
'S':45,
'T':46,
'U':47,
'V':48,
'W':49,
'X':50,
'Y':51,
'Z':52
}

fileobj=open("day_3.txt")
allRucksacks=fileobj.read().split('\n')



def findValue (key):

	value = priority_dictionary[key]

	return value


#unfortunately the list set function in python removes duplicates
#this really harshed my mellow tbh
def intersection(list1,list2):

	commonElement = [item for item in list1 if item in list2]
	print(commonElement)

	return commonElement[0]


def partOne(fileInput):

	totalSum = 0

	for currentRucksack in allRucksacks:

		totalSize = len(currentRucksack)
		halfSize = totalSize/2
		halfSizeMinusOne = halfSize-1
		
		print("The current rucksack contains:",currentRucksack)
		print("It has",totalSize,"items")

		firstCompartment = currentRucksack[:int(halfSize)]
		print("This is the first compartment:",firstCompartment,"and it has this many elements:",len(firstCompartment))
		secondCompartment = currentRucksack[int(halfSize):]
		print("This is the second compartment",secondCompartment,"and it has this many elements:",len(secondCompartment))
		
		commonElement = intersection(firstCompartment,secondCompartment)
		print("The common element is:" , commonElement)
		print('\n')

		totalSum += priority_dictionary[commonElement]
		print("The priority sum is: ",totalSum)



#The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

#Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. 
#So, in the above example, the first group's rucksacks are the first three lines:


def partTwo(fileobj):
	#print(allRucksacks)

	allCombined = 0

	groups = ([allRucksacks[x:x+3] for x in range(0, len(allRucksacks), 3)])

	for currentGroup in groups:

		setA = set(currentGroup[0])
		setB = set(currentGroup[1])
		setC = set(currentGroup[2])

		badge = setA.intersection(setB,setC)
		badgeValue = list(map(findValue,badge))

		allCombined += badgeValue[0]

		print(allCombined)



partTwo(fileobj)
#partOne(fileobj)

