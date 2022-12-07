fileobj=open("sample_day6.txt")
datastream=list(fileobj.read())
print(datastream)

for x in range(len(datastream)-1):

	#for part 1 change this to 4 instead of 14
	setOfSignals = datastream[x:x+14]


	if(len(set(setOfSignals)) == len(setOfSignals)):

		print(set(setOfSignals))
		print(setOfSignals)
		#for part 1 change this to 4 instead of 14
		print("Signal found at:",x+14)
		exit()


	else:

		print(set(setOfSignals))
		print(setOfSignals)
		print("Signal not found!",x)
