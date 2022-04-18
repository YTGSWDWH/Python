x = -121
y = str(x)
str1 = "".join(y[len(y)-1-i] for i in range(len(y)))
print(str1)
ans = True if str1 == y else False
print(ans)