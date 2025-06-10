magazine = "hjibagacbhadfaefdjaeaebgi"
ransomNote = "adfae"

def canConstruct(magazine, ransomNote):

    magazine_freq = {}
    for i in magazine:
        magazine_freq[i] = magazine_freq.get(i,0)+1

    for j in ransomNote:
        if j not in magazine_freq:
            return False
        elif magazine_freq[j] == 1:
            del magazine_freq[j]
        else:
            magazine_freq[j] -= 1
    return True


print(canConstruct(magazine, ransomNote))