def reverseVowels(s):
    left = 0
    right = len(s) - 1

    list_s = list(s)
    def isVowel(ch):
        if ch.lower() == 'a':
            return True
        elif ch.lower() == 'e':
            return True
        elif ch.lower() == 'i':
            return True
        elif ch.lower() == 'o':
            return True
        elif ch.lower() == 'u':
            return True
        else:
            return False

    while(left < right):
        if isVowel(list_s[left]) and isVowel(list_s[right]):
            list_s[right], list_s[left] = list_s[left], list_s[right]
            left = left + 1
            right = right - 1
        elif isVowel(list_s[left]):
            right = right - 1
        elif isVowel(list_s[right]):
            left = left + 1
        else:
            left = left + 1
            right = right - 1

    return "".join(list_s)

s = "leetcode"
print(reverseVowels(s))