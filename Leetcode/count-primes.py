def countPrimes(n):
    def isPrimes(a):
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False
        return True
    count = 0
    for each in range(2, n):
        if isPrimes(each):
            print(each)
            count += 1
    return count

n = 20
print(countPrimes(n))