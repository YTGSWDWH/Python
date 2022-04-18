def findComplement(num):
    list1 = []
    value = 0
    while num != 0:
        list1.append((num % 2) ^ 1)
        num = num // 2
    str1 = "".join([str(each) for each in list1])
    for i in range(len(str1)):
        value = int(str1[i]) * 2**i + value
    return value

num = 1
print(findComplement(num))