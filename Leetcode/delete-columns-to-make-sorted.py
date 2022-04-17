def minDeletionSize(strs):
    list1 = [[row[i] for row in strs] for i in range(len(strs[0]))]
    print(list1)
    for i in range(len(list1)):
        if sorted(list1[i]) != list1[i]:
            return i

strs = ["zyx","wvu","tsr"]
print(minDeletionSize(strs))