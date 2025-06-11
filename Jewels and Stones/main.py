jewels = "zZz"
stones = "Z"

def numJewelsInStones(jewels, stones):
    jewels_set = set(jewels)

    jewel_total = 0
    for i in stones:
        if i in jewels_set:
            jewel_total += 1
    return jewel_total
print(numJewelsInStones(jewels, stones))