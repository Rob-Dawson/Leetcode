"""
This is solved by using the absolute function which converts all numbers to positive
Therefore, -4 becomes 4
This then means that -4 becomes 4 away from 0

For the edge condition where closest is the same, i.e. -1,1
Check if the condition exists using absolute
if exists, take the original number and check if it is greater than closest
"""

nums = [-10, 10, 10, 10]
# nums = [-4,-2,1,4,8]
# nums = [-1,1]
# nums = [2,1,1,-1,100000]
closest = nums[0]
distance = abs(nums[0])
nums.sort()
for i, j in enumerate(nums):
    if abs(j) < abs(closest):
        closest = j
        distance = abs(j)
    if abs(j) == abs(closest):
        if j > closest:
            closest = j
print(closest)
