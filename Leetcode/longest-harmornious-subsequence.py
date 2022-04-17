import collections


nums = [1,1,1,1]
nums_set = set(nums)
nums_count = dict(collections.Counter(nums))
print(nums_count)
res = 0
for each in nums_set:
    if each+1 in nums_set:
        res = max(res, nums_count[each]+nums_count[each+1])
print(res)
