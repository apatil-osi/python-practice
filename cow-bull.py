## -- Problem URL: https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

import random

def cowbull(userGuess):
    guessList = list(str(userGuess))
    randNum = random.randint(1000,9999)
    print(randNum)
    randList = list(str(randNum))
    cowBull = [0,0]
    if userGuess == randNum:
        cowBull[0] = userGuess
    else:
        for i in range(len(guessList)):
            if guessList[i] == randList[i]:
                cowBull[0] += 1
            elif guessList[i] in randList:
                cowBull[1] += 1
            else:
                continue
    return cowBull

def main():
    flag = 1
    while flag != 0:
        print("Welcome to the CowBull Game! Please enter a 4 digit number:")
        num = int(input())
        if len(str(num)) > 4:
            print("Your number has more than 4 digitis. Please try again .. ")
        
        else:
            gamList = (cowbull(num))
            if num in gamList:
                print("Congratulations! You guessed the correct number with all digits in the exact same place!")
                flag = 0

            elif gamList[0] == 0 and gamList[1] == 0:
                print("None of the digits in the number match .. Your guess was way off...")
        
            else:
                print("You have",gamList[0],"Cows and",gamList[1],"Bulls...")

if __name__ == "__main__":
    main()





