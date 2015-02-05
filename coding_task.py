import math 

c = [46., 64., 98., 99., 101., 104., 106., 107., 109., 110., 111., 111., 111., 115., 115.]
capital = 1000.
start = 1
end = 260

# compute every element in time series
def sum_sins(t):
	sin_ct = [math.sin(elm*t) for elm in c]
	return sum(sin_ct)

# compute time series
timeSeries = [100 + sum_sins(elm) for elm in range(start, end + 1)]

#print "Time series is: ", timeSeries
#print "Length of Time series: ", len(timeSeries)

#compute raw returns
rawReturns = []
previousPrice = timeSeries[0]
for currentPrice in timeSeries:
	rawReturns.append(currentPrice/previousPrice)
	previousPrice = currentPrice

#print "Raw returns are: ", rawReturns

# initialize strategy list containing actions and prices
strategy = []

#initialize indicator of whether stock is currently held or not
holding = False

#compute strategy
for elm in timeSeries:
	if holding == False:
		if elm >= 98. and elm <= 101.:
			strategy.append("B")
			holding = True
			continue
		else:
			strategy.append("N")
	if holding == True:
		if elm < 98. or elm > 101.:
			strategy.append("S")
			holding = False
			continue
		else:
			strategy.append("N")

#print "Strateg is: ", strategy
#print "Length of strategy period: ", len(strategy)

#re-initialize indicator of whether stock is currently held or not
holding = False

#compute daily raw returns
dailyRawReturns = []
for elm in range (start -1 ,end):
	if holding == True:
		if strategy[elm] == "N":
			dailyRawReturns.append(rawReturns[elm])
		elif strategy[elm] == "S":
			dailyRawReturns.append(rawReturns[elm])
			holding = False
			continue
	if holding == False:
		if strategy[elm] == "B":
			dailyRawReturns.append(0.)
			holding = True
			continue
		elif strategy[elm] == "N":
			dailyRawReturns.append(0.)

print "Daily raw returns are: ", dailyRawReturns
print "Number of days: ", len(dailyRawReturns)

# main function for testing
if __name__ == "__main__":
    main() 

