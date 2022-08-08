def almostEqual(diff, decPlaces):
    return abs(diff) < 10**(-decPlaces)

#Apparently x was supposed to be the number you're trying to find the square root of, not num-guess**2
#and the recursive equation was supposed to be (g + x/g)/2, not g + (x/g)/2
#the stepCount variable and print statements are for debugging porpoises
def guessSquareRoot(num, guess, decPlaces, stepCount):
    diff = num - guess**2
    #If the approximate square root is found
    if (almostEqual(diff, decPlaces)):
        #Tell the user when that the square root is found and return it
        print("Got square root for 2 as " + str(guess) + " in " + str(stepCount) + " steps.")
        return guess

    #While the square root hasn't been found to the desired accuracy
    if (not almostEqual(diff, decPlaces)):
        print(guess**2)
        stepCount += 1
        #improve the guess
        guess = guess + (diff/guess)/2
        return guessSquareRoot(num, guess, 4, stepCount)

#run test cases
for value in range(2, 7):
    guessSquareRoot(value**2, 1, 4, 0)