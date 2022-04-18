def hasAlternatingBits(n):
    n_bin = bin(n)[2:]
    if len(n_bin) == 1:
        return True
    elif len(n_bin) == 2:
        return n_bin[0] != n_bin[1]
    for i in range(len(n_bin)-1):
        print(n_bin[i],n_bin[i+1])
        if n_bin[i] == n_bin[i+1]:
            return False
    return True

n = 11
print(hasAlternatingBits(n))