nums = [1, 2, 3, 4]

"""
Example 1
Brute Force
    Solves the problem but results in time out
"""


def contains_duplicate_brute_force():
    """Loops through nums and returns true if a duplicate and false if there are no duplicates"""
    for i, num1 in enumerate(nums):
        for _, num2 in enumerate(nums[i + 1], start=i + 1):
            if num1 == num2:
                return True
    return False


contains_duplicate_brute_force()
