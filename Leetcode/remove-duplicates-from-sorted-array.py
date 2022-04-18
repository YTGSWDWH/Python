nums = [1,1,1,1,2,3]

for each in nums:
    while nums.count(each) != 1:
        nums.remove(each)
print(len(nums),nums)