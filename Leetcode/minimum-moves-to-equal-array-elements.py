def minMoves(nums):
    if len(set(nums)) == 1:
        return 0
    count = 0
    while len(set(nums)) != 1:
        max_index = nums.index(max(nums))
        for i in range(len(nums)):
            if i != max_index:
                nums[i] = nums[i] + 1
        count = count + 1
        print(nums)
    return count

nums = [1,100,5,9,3]
print(minMoves(nums))