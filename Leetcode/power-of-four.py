def isPowerOfFour(n):
    if n & (n-1) == 0 and bin(n).count('0') % 2 == 1:
        return True
    else:
        return False

n = -16
print(isPowerOfFour(n))