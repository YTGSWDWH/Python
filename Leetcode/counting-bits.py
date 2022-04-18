def countBits(n):
    list1 = []
    for i in range(n+1):
        list1.append(bin(i).count('1'))
    return list1

n = 5
print(countBits(n))