

fileobj=open("day_1.txt")
lines=fileobj.read().split('\n')


def getTotals(lines):

    newSum = 0
    totals = []

    for values in lines:

        if values != '':
            newSum = newSum + int(values)

        else:
            totals.append(newSum)
        
            newSum = 0


    return totals;



def getTopThree(totals):

    totals.sort(reverse = True)

    topThree = totals[0]+totals[1]+totals[2]

    return topThree




newTotals = getTotals(lines)

print("This is my max:", max(newTotals))

print("These are my top three:",getTopThree(newTotals))
