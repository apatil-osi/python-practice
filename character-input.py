### --- Problem URL: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import datetime
def char_input(name, age, num):
    date = datetime.datetime.now()
    year_diff = 100 - age
    year_100 = date.year + year_diff

    for i in range(0, num):
        print("Hello" , name, "You will turn 100 years old in ", year_100)

if __name__ == "__main__":
    print("Please enter your Name")
    name = str(input())

    print("Please enter your age")
    age = int(input())

    ## Extras 1.
    print("Please enter your fav number")
    num = int(input())

    char_input(name, age, num)

