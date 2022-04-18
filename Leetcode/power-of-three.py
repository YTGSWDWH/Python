def isPowerOfThree(n):
    if n < 3:
        if n == 1:
            return True
        else:
            return False
    return isPowerOfThree(n/3)

n = 9
print(isPowerOfThree(n))