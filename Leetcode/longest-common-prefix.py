strs = ["flower", "flow", "flight"]
list1 = []
min_len = 4
ans1 = "".join([strs[0][i] for i in range(min_len) if strs[0][i] == strs[1][i] == strs[2][i]])
for i in range(min_len):
    if strs[0][i] == strs[1][i] == strs[2][i]:
        # list1.append(strs[0][i])
        ans2 = "".join(strs[0][i])
# ans2 = "".join(list1)
print(ans1)
print(ans2)