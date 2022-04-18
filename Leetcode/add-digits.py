def addDigits(num):
    list1 = []
    while(num != 0):
        list1.append(num %  10)
        num = num // 10
    while(sum(list1) >= 10):
        num = sum(list1)
        list1.clear()
        while(num != 0):
            list1.append(num %  10)
            num = num // 10
        print(list1)
    return sum(list1)

num = 399
print(addDigits(num))