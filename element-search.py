## -- Problem URL: https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
import random
import timeit
def search(item, nums):
    mid = int(len(nums)/2)
    # found = 1
    # while found != 0:
    if item == nums[mid]:
        #found = 0
        return True
    elif item < nums[mid]:
        if item in nums[:mid]:
                #found = 0
            return True
        else:
            return False
    elif item > nums[mid]:
        if item in nums[mid:]:
                #found = 0
            return True
        else:
            return False
    else:
        #found = 0
        return False

def main():
    nums = []
    print("Please enter the length of the list.")
    listLen = int(input())
    for i in range(listLen):
        nums.append(random.randint(0, listLen))
    sortedNums = nums.sort()
    #print("Sorted list has been generated:", nums)

    print("Please enter the number to search in this list")
    item = int(input())
    
    found = search(item, nums)
    
    if found == True:
        print("Your number is present in this list")
    #elif item  not in sortedNums:
    else:
        print("Your element is not present in this list")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Program Run Time: ', stop - start)  