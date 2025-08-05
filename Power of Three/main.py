def is_power_of_three(value):
    if value == 1:
        return True
    elif value < 1 or value % 3 != 0:
        return False
    return is_power_of_three(value//3)

def main():
    n = 27
    print(is_power_of_three(n))


if __name__ == "__main__":
    main()