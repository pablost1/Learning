# 581. Shortest Unsorted Continuous Subarray
# Fails for:
# [1,3,2,2,2]

def findUnsortedSubarray(nums=[]):
    coda = []
    last_num = nums[0]
    for current_num in nums:
        if current_num == last_num:
            continue
        elif current_num < last_num:
            coda.append(nums.index(current_num))
            last_num = current_num
        else:
            last_num = current_num
            
    return (coda[-1]-coda[0])+2

if __name__ =="__main__":

    print(findUnsortedSubarray([1,3,2,2,2]))
