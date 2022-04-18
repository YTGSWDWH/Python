x = -2147483412
sign = x < 0 and -1 or 1
x = abs(x)

ans = 0

while x != 0:
    ans = ans * 10 + x % 10
    x = x // 10

if ans > (1<<31)-1:
    ans = 0
else:
    ans = sign * ans
print(ans)