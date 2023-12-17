#number guessing game

import random
import math
lowerBound = int(input("Enter lower bound number: "))
upperBound = int(input("Enter upper bound number: "))
randomNumber = random.randint(lowerBound,upperBound)
numberOfGuesses = round(math.log((upperBound - lowerBound + 1), 2))

while numberOfGuesses > 0:
    print("Total number of guesses remaining, ", numberOfGuesses)
    guessedNumber = int(input("Guess the number: "))
    numberOfGuesses = numberOfGuesses - 1
    if(guessedNumber > randomNumber):
        print("Try again! You guessed too high")
    elif(guessedNumber < randomNumber):
        print("Try again! you guessed too small")
    elif(guessedNumber == randomNumber):
        print("Congratulations you did it in ",numberOfGuesses)


