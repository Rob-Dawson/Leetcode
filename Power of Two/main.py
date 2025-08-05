#Going Down
def is_power_of_two(value):
    if value == 1:
        return True
    elif value < 1 or value % 2 != 0:
        return False
    return is_power_of_two(value//2)

#Going Up
def is_power_of_two_up(value, current=1):
    if current == value:
        return True
    elif current > value:
        return False
    return is_power_of_two_up(value, current=current*2)

def main():
    n = 1
    print(is_power_of_two(n))
    print(is_power_of_two_up(n))


if __name__ == "__main__":
    main()