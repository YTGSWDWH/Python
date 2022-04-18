def isSubsequence(s, t):
    if len(s) == 0:
        return True
    left = 0
    right = 0
    while right < len(t) and left < len(s):
        if t[right] == s[left]:
            left = left + 1
            right = right + 1
            if left == len(s):
                return True
        else:
            right = right + 1
        print(left, right)
    if right == len(t):
        return False

s = ""
t = "ahbgdc"
print(isSubsequence(s, t))