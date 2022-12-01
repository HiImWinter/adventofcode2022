

fileobj=open("day_1.txt")
lines=fileobj.read().split('\n')


def getTotals(lines):

    index = 0
    totals = []

    for values in lines:

        if values != '':
            index = index + int(values)

        else:
            totals.append(index)
        
            index = 0


    return totals;



def getTopThree(totals):

    totals.sort(reverse = True)

    topThree = totals[0]+totals[1]+totals[2]

    return topThree




newTotals = getTotals(lines)

print("This is my max:", max(newTotals))

print("These are my top three:",getTopThree(newTotals))



   