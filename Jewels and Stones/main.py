jewels = "Z"
stones = "Z"
jewels_set = set()

for i in jewels:
    jewels_set.add(i)

jewel_total = 0
for i in stones:
    if i in jewels_set:
        jewel_total += 1
print(jewel_total)