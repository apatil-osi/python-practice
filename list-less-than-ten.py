
import time

def listcheck(nums, new_nums):
    
    print("All list elements less than 5 are:")
    for i in nums:
        if i < 5: 
            #print(i)
            new_nums.append(i)

        else:
            continue
        #display()
    print(new_nums)

# def display():
#     time.sleep(1)
#     print(".")

def userFunc(nums, userNum):
    userList = []
    for i in nums:
        if i < userNum:
            userList.append(i)
    userList.sort()
    print("List with elements smaller than", userNum, "is", userList)

if __name__ == "__main__":

    nums = []
    new_nums = []

    print("Please enter the length of the list:")
    numsLen = int(input())

    print("Proceed to enter new elements:")
    for i in range(numsLen):
        num = int(input())
        nums.append(num)

    listcheck(nums, new_nums)

    print("Enter a number to compare list elements..")
    userNum = int(input())

    userFunc(nums, userNum)
    