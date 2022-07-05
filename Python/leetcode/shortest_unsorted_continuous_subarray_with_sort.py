# 581. Shortest Unsorted Continuous Subarray
# Fails for:
# [1*10000]

def qs(array):
    if len(array) == 0:
        return []
    else:
        pivot = array.pop(0)
        left = [x for x in array if x<=pivot]
        right = [y for y in array if y>pivot]
        return qs(left)+[pivot]+qs(right)

def findUnsortedSubarray(nums=[]):
    coda = []
    if len(nums)==1 or len(nums)==0:
        return 0
    sorted_array = qs(nums[:])
    coda = []

    i=0
    while i <= len(nums)-1:
        if nums[i] != sorted_array[i]:
            coda.append(i)
        i+=1
    
    return (coda[-1]-coda[0])+1

if __name__ =="__main__":

    print(findUnsortedSubarray([2,6,4,8,10,9,15]))
