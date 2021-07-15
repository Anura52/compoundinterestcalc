
initialCapital = int(input("How much capital do you have? (in USD)\n> "))

timeModifierFloat = 24.0
timeModifierInt = int(timeModifierFloat)
dailyInterest = float(input("What daily returns do you expect? (%)\n> "))
interestRate = (dailyInterest/100)/timeModifierFloat

idealAmtOfComps = 4
intervalForOptimum = 0.1
calculateUpTo = 300
startNumOfDays = 1

comissionFee = 0.001
gasFee = float(input("What gas fees do you expect per compound? (in USD)\n> "))


def compound(capital, rewards):
    capital += rewards*(1.0-comissionFee) - gasFee
    rewards = 0.0
    return capital, rewards


def runSimulation(rewardValue, numOfDays):
    dayCount = 1
    amtCompounded = 0
    rewards = 0.0
    capital = initialCapital
    totalTime = numOfDays*timeModifierInt
    while dayCount <= totalTime:
        rewards += capital * interestRate
        if rewards > rewardValue:
            capital, rewards = compound(capital, rewards)
            amtCompounded += 1
        dayCount += 1
    if rewards > gasFee:    #This modifies final result only slightly. It's to avoid the program trying to stack rewards to avoid paying an extra gas fee
        capital, rewards = compound(capital, rewards)
        amtCompounded += 1
    return capital, amtCompounded      #If the last compound isn't implemented, then it should return capital+rewards instead of capital


def calculateOptimum(numOfDays):
    i = 1.0
    max_i = 0.0
    maxCapital = 0.0
    maxAmtCompounded = 0
    provCapital = 0.0
    provAmtCompounded = 0
    while i <= calculateUpTo:
        provCapital, provAmtCompounded = runSimulation(i, numOfDays)
        if provCapital > maxCapital:
            maxCapital = provCapital
            maxAmtCompounded = provAmtCompounded
            max_i = i
        i += intervalForOptimum
    return max_i, maxCapital, maxAmtCompounded


def calculateOptimalTimeframe():
    runningNumOfDays = startNumOfDays
    optimalNumOfDays = -1
    optimalCapital = -1
    numOfCompounds = -1
    while numOfCompounds <= idealAmtOfComps:
        sellAt, finalCapital, numOfCompounds = calculateOptimum(runningNumOfDays)
        if numOfCompounds == idealAmtOfComps:
            if finalCapital > optimalCapital:
                optimalCapital = finalCapital
                optimalNumOfDays = runningNumOfDays
        runningNumOfDays += 1
    return optimalNumOfDays


idealNumOfDays = calculateOptimalTimeframe()
sellAt, finalCapital, totalCompounds = calculateOptimum(idealNumOfDays)

print(f"Then you should compound at {sellAt}. This was calculated with a {idealNumOfDays} days period.")
print(f"You will get ${finalCapital} after that time. You will do {totalCompounds} compounds.")
#print(f"You will get ${finalCapital}, of which ${amtInRewards} are still in rewards.\nThere have been {totalCompounds} compounds.")

print("Done.")
