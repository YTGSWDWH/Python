def countPrimes(n):
    is_prime = [True]*(n)
    ans = 0
    for num in range(2,n):
        for k in range(2,(n-1)//num+1):
            is_prime[num*k]=False
    for i in range(2,n):
        if is_prime[i]:
            ans += 1
    return ans

n = 20
print(countPrimes(n))