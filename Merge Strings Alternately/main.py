word1 = "abcd"
word2 = "pq"
merged = []
word1Len = len(word1)
word2Len = len(word2)
totalLen = word1Len + word2Len
word1Count = 0
word2Count = 0

while len(merged) < totalLen:
    if word1Count < word1Len:
        merged.append(word1[word1Count])
        word1Count+=1
    if word2Count < word2Len:
        merged.append(word2[word2Count])
        word2Count +=1 

print(merged)