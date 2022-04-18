def toHex(num):
    list1 = []
    if num == 0:
        list1.append(0)
    elif num < 0:
        num = num & 0xFFFFFFFF
    while num != 0:
        list1.append(num % 16)
        num = num // 16
    list1.reverse()
    for i in range(len(list1)):
        if list1[i] >= 10:
            list1[i] = chr(list1[i] + 87)
    return "".join([str(each) for each in list1])

num = -1
print(toHex(num))