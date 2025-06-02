# new_sentence = ""

# sentence = "A man, a plan, a canal, Panama!!"

# formattedSentence = "".join(c for c in sentence if c.isalpha())
# print(formattedSentence)

# formattedSentence = formattedSentence.lower()
# for i in range(len(formattedSentence), 0, -1):
#     new_sentence += formattedSentence[i - 1]
# if formattedSentence == new_sentence:
#     print("yes")
# print(new_sentence)
# print(formattedSentence)


def isPalendrome(sentence):
    
    formatted = [c.lower() for c in sentence if c.isalnum()]
    l = 0
    r = len(formatted)-1
    while l<r:
        if formatted[l].isalnum() and formatted[r].isalnum():
            
            l+=1
            r-=1
        else:
            return False
    return True    

def isPalendromeNoVariable(sentence):
    
    l = 0
    r = len(sentence)-1
    while l<r:
        if not sentence[l].isalnum():
            l+=1
            continue
        if not sentence[r].isalnum():
            r-=1
            continue
        if sentence[l].lower() != sentence[r].lower():
            return False
        l+=1
        r-=1
    return True

# print(isPalendrome("0P"))
print(isPalendromeNoVariable("A man, a plan, a canal: Panama"))
