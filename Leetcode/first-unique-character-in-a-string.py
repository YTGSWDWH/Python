import collections
from typing import Collection

def firstUniqChar(s):
    for i in range(len(s)):
        if s[i] not in s[:i] + s[i+1:]:
            return i

s = "leetcode"
frequency = collections.Counter(s)
print(frequency)
print(firstUniqChar(s))