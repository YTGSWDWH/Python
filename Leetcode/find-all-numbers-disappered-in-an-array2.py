def findDisappearedNumbers(nums):
    n = len(nums)
    for num in nums:
        x = (num - 1) % n
        nums[x] += n
    ret = [i + 1 for i, num in enumerate(nums) if num <= n]
    return ret

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))