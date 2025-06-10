import timeit

nums = [1, 2, 3, 4]

# """
# Example 1
# Brute Force
#     Solves the problem but results in time out
# """


def contains_duplicate_brute_force():
    """Loops through nums and returns true if a duplicate and false if there are no duplicates"""
    for i, num1 in enumerate(nums):
        for _, num2 in enumerate(nums[i + 1 :], start=i + 1):
            if num1 == num2:
                return True
    return False


# """
# Example 2
# Hashset
#     Solves the problem
# """


def contains_duplicate_hash_table():
    """Loops through nums and checks if the number exists in the hash set.
    Return True if exists
    Adds number to hash set if number does not exist
    """
    number_hash = {}
    for i in nums:
        if i in number_hash:
            return True
        number_hash[i] = i
    return False


# """
# Example 3
# Using Sort
#     Solves the problem
# """


def contains_duplicate_sort():
    """
    Sorts the list first and then compares the current value with the next value
    """
    nums.sort()
    for i, num1 in enumerate(nums[:-1]):
        if num1 == nums[i + 1]:
            return True
    return False


def contains_duplicate_set():
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False

def contains_duplicate_set_len():
    return (len(nums) != len(set(nums)))


# result = scontains_duplicate_brute_force()
# result = contains_duplicate_hash_table()
# result = contains_duplicate_sort()
# print(result)

contains_duplicate_brute_force = timeit.timeit(
    stmt="contains_duplicate_brute_force()",
    globals=globals(),
    number=100000
)
contains_duplicate_hash_table = timeit.timeit(
    stmt="contains_duplicate_hash_table()",
    globals=globals(),
    number=100000
)

contains_duplicate_sort = timeit.timeit(
    stmt="contains_duplicate_sort()",
    globals=globals(),
    number=100000
)
contains_duplicate_set = timeit.timeit(
    stmt="contains_duplicate_set()",
    globals=globals(),
    number=100000
)

contains_duplicate_set_len = timeit.timeit(
    stmt="contains_duplicate_set_len()",
    globals=globals(),
    number=100000
)

print(f"contains_duplicate_brute_force method:  {contains_duplicate_brute_force:.4f} seconds")
print(f"contains_duplicate_hash_table method:  {contains_duplicate_hash_table:.4f} seconds")
print(f"contains_duplicate_sort method:  {contains_duplicate_sort:.4f} seconds")
print(f"contains_duplicate_set method:  {contains_duplicate_set:.4f} seconds")
print(f"contains_duplicate_set_len method:  {contains_duplicate_set_len:.4f} seconds")