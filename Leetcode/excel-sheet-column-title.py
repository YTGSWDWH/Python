def convertToTitle(columnNumber):
    list1 = []
    while columnNumber != 0:
        if columnNumber == 26:
            list1.append(26)
            break
        elif columnNumber % 26 == 0:
            list1.append(26)
        else:
            list1.append(columnNumber % 26)
        columnNumber = (columnNumber - 1) // 26
    list1.reverse()
    for index, value in enumerate(list1):
        list1[index] = chr(value + 64)
    str1 = "".join([str(each) for each in list1])
    return str1
columnNumber = 702
print(convertToTitle(columnNumber))