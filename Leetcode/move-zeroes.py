def moveZeroes(nums):
    numsOfZero = nums.count(0)
    for i in range(numsOfZero):
        nums.remove(0)
    for i in range(numsOfZero):
        nums.append(0)
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))