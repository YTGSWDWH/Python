strs = ["flower", "flow", "flight"]
list1 = []
min_len = len(strs[0])

for i in range(len(strs)):
    if(len(strs[i]) < min_len):
        min_len = len(strs[i])
flag = True
i = 0
while i < min_len:
    j = 0
    while j < len(strs) - 1:
        if(strs[j][i] != strs[j+1][i]):
            flag = False
        j = j + 1
    if(flag):
        list1.append(strs[0][i])
    i = i + 1
ans = "".join(list1)
print(ans)