n = 4

def arrange(i, n):
    numerator = 1
    denominator = 1
    for index in range(n-i+1,n+1):
        numerator = numerator * index
    for index in range(1,i+1):
        denominator = denominator * index
    return numerator//denominator


ans = 0
for i in range(n//2 + 1):
    ans = ans + arrange(i, n-i)
print(ans)