def findContentChildren(g, s):
    left = 0
    right = 0
    count = 0
    g.sort()
    s.sort()
    while right < len(s) and left < len(g):
        if s[right] >= g[left]:
            count = count + 1
            right = right + 1
            left = left + 1
        else:
            right = right + 1
    return count

g = [2,2,3,4]
s = [1,2,3]
print(findContentChildren(g, s))