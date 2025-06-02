def summaryRanges(nums):
    answer = []
    if len(nums) == 0:
        return answer
    start = nums[0]
    for i in range(len(nums)):
        if i+1 >= len(nums):
            if start == nums[i]:
                answer.append(f"{start}")
            else:
                answer.append(f"{start}->{nums[i]}")
        elif nums[i+1] != nums[i]+1:
            if start == nums[i]:
                answer.append(f"{start}")
                start = nums[i+1]
            else:
                answer.append(f"{start}->{nums[i]}")
                start = nums[i+1]
    return answer


def summaryRangesFancy(nums):
    answer = []
    i=0
    while i < len(nums):
        start = nums[i]
        while i < len(nums) -1 and nums[i] + 1 == nums[i+1]:
            i+=1
        if start != nums[i]:
            answer.append(f"{start}->{nums[i]}")
        else:
            answer.append(f"{nums[i]}")
        i+=1
    return answer





nums = [0,1,2,4,5,7]
print(summaryRanges(nums))
print(summaryRangesFancy(nums))