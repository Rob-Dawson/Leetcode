digits = [1, 2, 3]


def plus_one():
    for i, num in reversed(list(enumerate(digits))):
        if num == 9:
            for j, num1 in reversed(list(enumerate(digits[: i + 1]))):
                if num1 == 9:
                    digits[j] = 0
                    if j == 0:
                        digits.insert(0, 1)
                        return
                else:
                    digits[j] = digits[j] + 1
                    return
        else:
            digits[i] = digits[i] + 1
            return


plus_one()
print(digits)
