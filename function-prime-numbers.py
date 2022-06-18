
## Problem URL: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

import timeit
from tracemalloc import stop

div = []

def prime(num):
    flag = 0
    #div = []
    for i in range(1, num+1):
        if num % i == 0:
            flag += 1
            div.append(i)
        else:
            continue
    return flag

def main():
    print("Please enter your number:")
    num = int(input())

    divisors = prime(num)

    if divisors > 2:
        print(num, "is NOT a prime number ... It has", divisors, "divisors ... List of divisors:", div)
    elif divisors == 0:
        print(num, "is netier a Prime number, nor a Non-Prime number ... It is the begining of everything .. It has", divisors, "divisors ... List of divisors:", div)
    else:
        print(num, "is a PRIME number ... It has", divisors, "divisors ... List of divisors:", div)
    

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Program Run Time: ', stop - start)