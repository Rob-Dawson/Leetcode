s = "acb"
t = "ahbgdc"
print(len(s))
def isSub(s,t):
    j = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            j+=1
            if j==len(s):
                return True
    return False

print(isSub(s,t))