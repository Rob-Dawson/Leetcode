roman = {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}

s = "MCMXCIV"
number = 0
for i in range(len(s)):
    currentNumber = roman.get(s[i])

    if len(s) > i+1 and currentNumber < roman.get(s[i+1]):
        number -= currentNumber
    else:
        number += currentNumber
print(number)