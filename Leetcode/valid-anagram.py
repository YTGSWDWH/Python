def isAnagram(s, t):
    if set(s) != set(t):
        return False
    else:
        for each in set(s):
            if s.count(each) != t.count(each):
                return False
        return True

s = "aacc"
t = "ccac"
print(isAnagram(s, t))