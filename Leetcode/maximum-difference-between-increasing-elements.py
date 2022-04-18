def maximumDifference(nums):
    min_nums = nums[0]
    max_diff = -1
    for i in range(len(nums)-1):
        max_nums = nums[-1]
        if nums[i] < min_nums:
            min_nums = nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] > max_nums:
                max_nums = nums[j]
        print(min_nums,max_nums)
        if max_nums - min_nums > max_diff:
            max_diff = max_nums - min_nums
    return max_diff

nums = [9,4,3,2]
print(maximumDifference(nums))