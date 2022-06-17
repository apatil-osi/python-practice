## -- Problem URL: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

def divisor(num):
    
    print("All the Divisors for", num, "are:")
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
        else:
            continue
    
if __name__ == "__main__":
    
    print("Please enter the number for which you want to see all the divisors")
    num = int(input())

    divisor(num)