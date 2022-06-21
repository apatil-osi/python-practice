## --- Problem URL: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

def listDupes(nums):
    newList = []
    for i in nums:
        if i not in newList:
            newList.append(i)
        else:
            continue
    return sorted(newList)

def setDupes(nums):
    newList = [i for i in set(nums)]
    return newList

def main():
    nums = [1,6,2,7,1,2,7,8,3,89,1,4,8,3,0,3,6,7,8,4]
    print("Solution without SETS", listDupes(nums))
    print("Solution with SETS",setDupes(nums))

if __name__ == "__main__":
    main()