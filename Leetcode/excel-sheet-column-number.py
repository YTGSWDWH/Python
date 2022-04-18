def titleToNumber(columnTitle):
    num = 0
    for index, value in enumerate(columnTitle[::-1]):
        num = (ord(value) - 64) * 26**(index) + num
    return num

columnTitle = "ZY"
print(titleToNumber(columnTitle))