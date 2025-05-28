s = "acb"
t = "ahbgdc"
print(len(s))
def isSub(s,t):
    if len(s) <= 0:
        return True
    if len(t) <= 0:
        return False
    j = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            j+=1
            if j==len(s):
                return True
    return False

print(isSub(s,t))