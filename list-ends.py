## -- Problem URL: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

import random

def listEnds(nums):
    start = nums[0]
    end = nums[len(nums)-1]
    newList = [start, end]
    return newList

def main():
    nums = [i for i in range(random.randint(1,10))]
    print("OG list:", nums)
    newList = listEnds(nums)
    print("List with first and last element of the first list:", newList)

if __name__ == "__main__":
    main()