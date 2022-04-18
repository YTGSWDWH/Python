def hammingDistance(x, y):
    z = x ^ y
    count = 0
    while z != 0:
        if z % 2 == 1:
            count = count + 1
        z = z // 2
    return count

x = 1
y = 3
print(x ^ y)
print(hammingDistance(x, y))