## --- Problem URL: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def fibonnaci(nums):
    fibo = [0,1]
    for i in range(nums):
        if i >= 2:
            fibo.append(fibo[i-2] + fibo[i-1])
        else:
            continue
    return fibo
def main():
    print("Please enter the number of fibo sequence you wish to see")
    nums = int(input())
    print("Fibonacci sequence: ", fibonnaci(nums))

if __name__ == "__main__":
    main()
