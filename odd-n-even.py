## -- Problem URL: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

def odd_even(num):
    if num % 2 == 0:
        if num % 4 == 0:
            print("The number entered,", num, "is an EVEN number AND a Multiple of 4..")
        else:
            print("Then number entered,", num, "is an EVEN number")
    else:
        print("Then number entered,", num, ", is an ODD number")

def mult_check(num, check):
    if num % check == 0:
        print(num, "is a multiple of", check)
    else:
        print(num, "is NOT a multiple of", check)

if __name__ == "__main__":
    print("Please enter a random number. I will tell you if it is EVEN or ODD..")
    num =int(input())

    odd_even(num)

    print("\nPlease enter a number you want to check for multiples of", num)
    check = int(input())

    mult_check(num,check)
