nums = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]

def sortedSquares(nums):
    sortedArray = []
    l = 0
    r = len(nums) -1
    while l<=r:
        if abs(nums[l]) > abs(nums[r]):
            sortedArray.append(nums[l]**2)
            l+=1
        else:
            sortedArray.append(nums[r]**2)
            r-=1
    sortedArray.reverse()
    return sortedArray

def sortedSquaresWithoutReverse(nums):
    sortedArray = [0] * len(nums)
    pos = len(nums)-1
    l = 0
    r = len(nums)-1
    while l<=r:
        if abs(nums[l]) > abs(nums[r]):
            sortedArray[pos] = nums[l]**2
            l+=1
        else:
            sortedArray[pos] = nums[r]**2
            r-=1
        pos-=1
    return sortedArray


print(sortedSquares(nums))
print(sortedSquaresWithoutReverse(nums))