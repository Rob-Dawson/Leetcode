strs = ["flower","flow","flight"]


def LeastCommon(strs):
    longest = 0
    counter = 0
    shortest = len(min(strs, key=len))
    while counter <= shortest -1:
        for i in strs:
            if i[counter] != strs[0][counter]:
                return (strs[0][:longest])
        longest+=1
        counter+=1
    return(strs[0][:longest])

print(LeastCommon(strs))