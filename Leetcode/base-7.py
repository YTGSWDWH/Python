def convertToBase7(num):
    list1 = []
    if num == 0:
        return "0"
    elif num > 0:
        while num != 0:
            list1.append(num % 7)
            num = num // 7
        list1.reverse()
        return "".join(str(each) for each in list1)
    else:
        while num != 0:
            num = abs(num)
            list1.append(num % 7)
            num = num // 7
        list1.append('-')
        list1.reverse()
        return "".join(str(each) for each in list1)

num = 0
print(convertToBase7(num))