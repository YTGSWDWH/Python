nums = [1,2,-3]

if len(nums) == 0:
    maxSum = 0
preSum = maxSum = nums[0]
for i in range(1, len(nums)):
    preSum = max(preSum + nums[i], nums[i])
    maxSum = max(maxSum, preSum)
print(maxSum)