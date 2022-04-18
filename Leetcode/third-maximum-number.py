def thirdMax(nums):
    nums_set = set(nums)
    if len(nums_set) < 3:
        return max(nums_set)
    else:
        nums_list = list(nums_set)
        nums_list.sort()
        nums_list.reverse()
    return nums_list[2]

nums = [2,1]
print(thirdMax(nums))