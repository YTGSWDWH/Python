import collections

def findTheDifference(s, t):
    frequency_s = collections.Counter(s)
    frequency_t = collections.Counter(t)
    

s = "a"
t = "aa"
print(findTheDifference(s, t))