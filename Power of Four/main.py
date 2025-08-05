def is_power_of_four(value):
    if value == 1:
        return True
    elif value < 1 or value % 4 != 0:
        return False
    return is_power_of_four(value//4)

def main():
    n = 27
    print(is_power_of_four(n))


if __name__ == "__main__":
    main()