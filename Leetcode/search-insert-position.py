nums = [1,3,5,6]
target = 7

if target in nums:
    ans = nums.index(target)
else:
    ans = 0
    for each in nums:
        if each < target:
            ans = ans + 1

print (ans)