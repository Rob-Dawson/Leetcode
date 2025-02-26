def majorityElement(nums):
    numbers = {}
    maxNum = 0
    maxOccurrence = 0

    for num in nums:
        if num in numbers:
            numbers[num] +=1
        else:
            numbers[num] = 1
    print(numbers)

    for num, occurrence in numbers.items():
        if occurrence > maxOccurrence:
            maxOccurrence = occurrence
            maxNum = num
    return maxNum
numbers=[1,2,3,3,3,3,4,5]
print(majorityElement(numbers))