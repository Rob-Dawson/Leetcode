def majorityElement(nums):
    numbers = {}
    
    for num in nums:
        if num in numbers:
            numbers[num] +=1
        else:
            numbers[num] = 1
    print(numbers)

numbers=[1,2,3,4,5]
majorityElement(numbers)