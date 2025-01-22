nums = [1, 2, 3, 4]

"""
Example 1
Brute Force
    Solves the problem but results in time out
"""


def contains_duplicate_brute_force():
    """Loops through nums and returns true if a duplicate and false if there are no duplicates"""
    for i, num1 in enumerate(nums):
        for _, num2 in enumerate(nums[i + 1 :], start=i + 1):
            if num1 == num2:
                return True
    return False


def contains_duplicate_hash_table():
    """Loops through nums and checks if the number exists in the hash table.
    Return True if exists
    Adds number to hash table if number does not exist
    """
    number_hash = {}
    for i in nums:
        if i in number_hash:
            return True
        number_hash[i] = i
    return False


# result = scontains_duplicate_brute_force()
result = contains_duplicate_hash_table()
print(result)
