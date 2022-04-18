def hammingWeight(n):
    nums = bin(n)[2:]
    print(nums)
    res = nums.count('1')
    return res

n = 0b11101
print(hammingWeight(n))