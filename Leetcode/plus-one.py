digits = [9]

ans = 0
for each in digits:
    ans = 10 * ans + each
ans = ans + 1

str1 = str(ans)
list1 = []
for each in str1:
    list1.append(int(each))
print(list1)