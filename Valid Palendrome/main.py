new_sentence = ""

sentence = "A man, a plan, a canal, Panama!"
formattedSentence = "".join(c for c in sentence if c.isalpha())
formattedSentence = formattedSentence.lower()
for i in range(len(formattedSentence), 0, -1):
    new_sentence += formattedSentence[i - 1]
if formattedSentence == new_sentence:
    print("yes")
print(new_sentence)
print(formattedSentence)
