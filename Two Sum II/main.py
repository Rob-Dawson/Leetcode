numbers = [-1,0]
target = -1


def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r-=1
        elif numbers[l] + numbers[r] < target:
            l+=1
        else:
            return [l+1, r+1]

print(twoSum(numbers, target))
