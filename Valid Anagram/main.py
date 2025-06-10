import timeit


s = "anagram"
t = "nagaram"

def isAnagram(s, t):
    freq_hash = {}
    for i in s:
        if i in freq_hash:
            number = freq_hash[i]+1
            freq_hash.update({i:number})
        else:
            freq_hash.update({i:1})

    for j in t:
        if j in freq_hash:
            number = freq_hash[j]
            freq_hash.update({j:number-1})
        else:
            return False
    if all(value == 0 for value in freq_hash.values()):
        return True
    else:
        return False

def isAnagramFaster(s, t):
    freq_hash = {}
    for i in s:
        freq_hash[i] = freq_hash.get(i,0)+1

    for j in t:
        if j not in freq_hash:
            return False
        elif freq_hash[j] == 1:
            del freq_hash[j]
        else:
            freq_hash[j]-=1
    return not freq_hash


is_anagram_timing = timeit.timeit(
    stmt="isAnagram(s, t)",
    globals=globals(),
    number=100000
)

is_anagram_faster_timing = timeit.timeit(
    stmt="isAnagramFaster(s, t)",
    globals=globals(),
    number=100000
)
print(f"is_anagram_timing method:  {is_anagram_timing:.4f} seconds")
print(f"is_anagram_faster_timing method:  {is_anagram_faster_timing:.4f} seconds")


# print(isAnagram(s, t))
# print(isAnagramFaster(s,t))