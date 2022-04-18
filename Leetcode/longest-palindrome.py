import collections

def longestPalindrome(s):
    len1 = 0
    frequency = collections.Counter(s)
    frequency = dict(frequency)
    for _, value1 in frequency.items():
        if value1 >= 2:
            if value1 % 2 == 0:
                len1 = len1 + value1
            else:
                len1 = len1 + value1 - 1
    for _, value2 in frequency.items():
        if value2 % 2 != 0:
            len1 = len1 + 1
            break
    return len1

s = "abccccdd"
print(longestPalindrome(s))