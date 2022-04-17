def fib(n):
    a = 0
    b = 1
    if n < 2:
        return n
    else:
        for i in range(n-1):
            a, b = b, a+b
    #return b % (1e9+7)
    #return b % 1000000007
    return b % int(1e9+7)

n = 81
nums = [1,2,4,5,6]
print(nums[::2])
print(fib(n))