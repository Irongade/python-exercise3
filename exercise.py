import random

isGuessOver = False

# Creating the Easy Level mode, that checks if answer from user is equal to randomly generated number, if equal, stops the loop and if not continues it


def easyLevel(randomGeneratedNumber, numberOfGuessesLeft):
    print(f"** welcome to the easy level. \n You have to guess a number between 1-10 **")
    answer = int(input("guess a number:"))
    if (randomGeneratedNumber != answer):
        print(
            f"** Sorry, that was wrong, Try Again. ** \n ** You have {numberOfGuessesLeft} guess remaining **")
        isGuessOver = False
        return isGuessOver
    elif (randomGeneratedNumber == answer):
        print("*** Congratulations, You got it right!!! ***")
        isGuessOver = True
        return isGuessOver

# Creating the Medium Level mode, that checks if answer from user is equal to randomly generated number, if equal, stops the loop and if not continues it


def mediumLevel(randomGeneratedNumber, numberOfGuessesLeft):
    print(f"** welcome to the medium level. \n You have to guess a number between 1-20 **")
    answer = int(input("guess a number:"))
    if (randomGeneratedNumber != answer):
        print(
            f"** Sorry, that was wrong, Try Again. ** \n ** You have {numberOfGuessesLeft} guess remaining **")
        isGuessOver = False
        return isGuessOver
    elif (randomGeneratedNumber == answer):
        print("*** Congratulations, You got it right!!! ***")
        isGuessOver = True
        return isGuessOver

# Creating the Hard Level mode, that checks if answer from user is equal to randomly generated number, if equal, stops the loop and if not continues it


def hardLevel(randomGeneratedNumber, numberOfGuessesLeft):
    print(f"** welcome to the hard level. \n You have to guess a number between 1-50 **")
    answer = int(input("guess a number:"))
    if (randomGeneratedNumber != answer):
        print(
            f" ** Sorry, that was wrong, Try Again. ** \n ** You have {numberOfGuessesLeft} guess remaining **")
        isGuessOver = False
        return isGuessOver
    elif (randomGeneratedNumber == answer):
        print("*** Congratulations, You got it right!!! ***")
        isGuessOver = True
        return isGuessOver

# this funtion checks the mode to be played by user and generates the random number, then initiates a loop that calls the game-level mode function
# It also ensures that the number of guesses is not exceeded.


def startGame(isGuessOver):
    print(f" ******* Welcome to `Guess a Number game!!!!` ******** \n *** There are 3 modes, Easy, Medium, Hard. ***")
    response = input("Easy/Medium/Hard. Pick one:")
    if (response.lower() == "easy"):
        numberOfGuessesLeft = 6
        randomGeneratedNumber = random.randint(1, 10)
        while (isGuessOver == False):
            if (numberOfGuessesLeft == 0):
                print(
                    f"*** The correct answer is {randomGeneratedNumber}, Sorry! ***")
                print(
                    "*******You have exhausted your number of guesses. Game Over!! (^_^) *******")
                isGuessOver = True
            else:
                numberOfGuessesLeft -= 1
                isGuessOver = easyLevel(
                    randomGeneratedNumber, numberOfGuessesLeft)
    elif (response.lower() == "medium"):
        numberOfGuessesLeft = 4
        randomGeneratedNumber = random.randint(1, 20)
        while (isGuessOver == False):
            if (numberOfGuessesLeft == 0):
                print(
                    f"*** The correct answer is {randomGeneratedNumber}, Sorry! ***")
                print(
                    "*******You have exhausted your number of guesses. Game Over!! (^_^) *******")
                isGuessOver = True
            else:
                numberOfGuessesLeft -= 1
                isGuessOver = mediumLevel(
                    randomGeneratedNumber, numberOfGuessesLeft)
    elif (response.lower() == "hard"):
        numberOfGuessesLeft = 3
        randomGeneratedNumber = random.randint(1, 50)
        while (isGuessOver == False):
            if (numberOfGuessesLeft == 0):
                print(
                    f"*** The correct answer is {randomGeneratedNumber}, Sorry! ***")
                print(
                    "*******You have exhausted your number of guesses. Game Over!! (^_^) *******")
                isGuessOver = True
            else:
                numberOfGuessesLeft -= 1
                isGuessOver = hardLevel(
                    randomGeneratedNumber, numberOfGuessesLeft)


# calling the game function
startGame(isGuessOver)
