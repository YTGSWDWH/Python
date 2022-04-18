def findDisappearedNumbers(nums):
    nums_set = set(nums)
    set1 = set([each for each in range(1,len(nums)+1)])
    print(nums_set, set1)
    return list(set1 - nums_set)

nums = [1,1]
print(findDisappearedNumbers(nums))