nums = [3,3]
target = 6

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i,j)
            
def twoSumHash(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        nums_dict[nums[i]] = i
    for i in range(len(nums)):
        y = target - nums[i]
        if y in nums_dict and nums_dict[y] != i:
            return (i, nums_dict[y])
        
print(twoSum(nums, target))
print(twoSumHash(nums, target))