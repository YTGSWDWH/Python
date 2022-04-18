def isIsomorphic(s, t):
    for i in range(len(s)):
        print(s.index(s[i]))
        print(t.index(t[i]))
        if s.index(s[i]) != t.index(t[i]):
            return False
    return True

s = "foo"
t = "bar"
print(isIsomorphic(s, t))