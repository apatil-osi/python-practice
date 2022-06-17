## -- Problem URL: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

from os import dup
import random

def overlap(numsLen, nums2Len):

    nums = []
    nums2 = []
    dups = []
    
    for i in range(numsLen):
        nums.append(random.randint(1,numsLen))

    print("Random generated list 1:", nums)

    for i in range(nums2Len):
        nums2.append(random.randint(1,nums2Len))

    print("Random generated list 2:", nums2)

    for i in nums:
        if i in nums2:
            if i in dups:
                continue
            else:
                dups.append(i)

    print("List with all duplicates from nums and nums2:", dups)

if __name__ =="__main__":

    print("Enter the len for list1 and list2:")
    numsLen = int(input())
    nums2Len = int(input())

    overlap(numsLen, nums2Len)
