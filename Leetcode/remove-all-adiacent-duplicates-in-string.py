def removeDuplicates(s):
    flag = False
    while not flag:
        len_s = len(s)
        for i in range(len_s-1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                break
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                flag = False
                break
        else:
            flag = True
    return s

s = "abbaca"
print(removeDuplicates(s))