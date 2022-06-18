## --- Problem URL: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
import random
def game():
    prompt = "Y"

    while prompt == "Y" or prompt == "y":
        print("Please enter your move (R/P/S) ...")
        move = str(input())

        compMove = ["R","P","S"]

        while move not in compMove:
            print("Invalid input. Please enter 'R', 'P' or 'S'")
            move = str(input())

        item = random.choice(compMove)
        
        if move == item:
            print("Your move was ", move, "and Computer's move was", item, " ... It is a Tie!")

        elif move == "R" and item == "P":
            print("Your move was Rock. But Computer's move was Paper. Sorry! You lose!")
        
        elif move == "P" and item == "S":
            print("Your move was Paper. But Computer's move was Scissors. Sorry! You lose!")

        elif move == "S" and item == "R":
            print("Your move was Scissors. But Computer's move was Rock. Sorry! You lose!")
        else:
            print("Your move was", move, "But Computer's move was", item, " ... Congratulations!! You win!!!")

        print("Would you like to play again? (Y/N)")
        prompt = str(input())

        if prompt == "Y" or prompt == "y":
            continue
        else:
            print("Goodbye! Nice playing with you!")
            break

def main():
    game()

if __name__ == "__main__":
    main()