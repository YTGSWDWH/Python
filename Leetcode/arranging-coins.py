def arrangeCoins(n):
    sum1 = 0
    i = 0
    if n == 0:
        return 0
    while sum1 <= n:
        i = i + 1
        sum1 = sum1 + i
    return i-1

n = 1
print(arrangeCoins(n))