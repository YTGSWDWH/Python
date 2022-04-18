def backtrack(first):
    # 所有数都填完了
    if first == n:  
        res.append(nums[:])
    for i in range(first, n):
        # 动态维护数组
        nums[first], nums[i] = nums[i], nums[first]
        # 继续递归填下一个数
        backtrack(first + 1)
        # 撤销操作
        nums[first], nums[i] = nums[i], nums[first]

nums = [1,2,3]
n = len(nums)
res = []
backtrack(0)
print(res)