haystack = "hello"
needle = "ll"

if len(haystack) == 0:
    ans = 0
elif needle not in haystack:
    ans = -1
else:
    ans = haystack.find(needle)

print(ans)