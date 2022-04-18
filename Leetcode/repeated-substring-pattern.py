def repeatedSubstringPattern(s):
    if len(s) == 1:
        return False
    for i in range(1, len(s)//2 + 1):
        if s[i] == s[0]:
            s_sub = s[0:i]
            print(s_sub)
            if len(s) % len(s_sub) == 0:
                multiple = len(s) // len(s_sub)
                if s_sub * multiple == s:
                    return True
    return False
    
s = "abcabcabc"
print(repeatedSubstringPattern(s))