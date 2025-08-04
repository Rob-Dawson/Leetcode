###Naive appraoch
nums = [1,2,3,4]
# nums = [0, 0]




def product_except_self_naive(numbers):
    new_list = []
    for i,_ in enumerate(numbers):
        temp = 1
        for j, value_j in enumerate(numbers):
            if i == j:
                continue
            temp *= value_j
        new_list.append(temp)
    return new_list

def product_except_self_prefix(numbers):
    prefix_prod = 1
    postfix_prod = 1
    n = len(numbers)
    prefix = [0] * n
    postfix = [0] * n

    for i in range(n):
        prefix[i] = prefix_prod
        prefix_prod *= numbers[i]
    for i in range(n-1,-1,-1):
        postfix[i] = postfix_prod
        postfix_prod *= numbers[i]

    return [prefix[i] * postfix[i] for i in range(n)]

def main():
    new_list = product_except_self_naive(nums)
    print(new_list)

    new_list = product_except_self_prefix(nums)
    print(new_list)
    


if __name__ == "__main__":
    main()
