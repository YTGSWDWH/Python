nums = [4,1,2,1,2]

""" for each in nums:
    if nums.count(each) == 1:
        print(each) """

for i in range(1, len(nums)):
    nums[0] ^= nums[i]   #和相同的数异或偶数次，结果不变
    print(nums[0])
print(nums[0])