
## -- Problem URL: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

from random import randint

def game():

    ctr = 0

    wish = "y"

    while wish == "y":
        num = randint(1,3)
        print("Please guess the generated number ...")
        guess = int(input())
        print(num)
        if num != guess:
            ctr += 1
            print("Incorrect guess! Enter EXIT to leave the game, YES(y) to continue ...")
            wish = str(input())

            if wish == "EXIT":
                print("Goodbye!!")
                break
            else:
                continue
        else:
            print("You guessed the correct number in", ctr, "attempts! Do you want to play again?! (Y for yes, EXIT for no)")
            wish = str(input())

            if wish == "EXIT":
                print("Goodbye!!")
                break
            else:
                continue


def main():
    game()

if __name__ == "__main__":
    main()