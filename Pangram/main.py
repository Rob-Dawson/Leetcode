alphabet = {
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
}


def check_if_pangram_hashset():
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    sentence = sentence.upper()
    for i in sentence:
        if i in alphabet:
            alphabet.remove(i)
    if len(alphabet) > 0:
        return False
    return True


# print(check_if_pangram_hashset())
