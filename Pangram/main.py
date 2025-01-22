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


def check_if_pangram_hashset_local_copy():
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    sentence = sentence.upper()
    local_alphabet = alphabet.copy()
    for i in sentence:
        if i in local_alphabet:
            local_alphabet.remove(i)
    if len(local_alphabet) > 0:
        return False
    return True


# print(check_if_pangram_hashset())
# print(check_if_pangram_hashset_local_copy())
