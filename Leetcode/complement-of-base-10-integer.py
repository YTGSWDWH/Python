def bitwiseComplement(n):
    n_bin = bin(n)[2:]
    n_bin_reverse = [0] * len(n_bin)

    for i in range(len(n_bin)-1):
        n_bin_reverse[i] = int(n_bin[i]) ^ 1
    return int("".join(str(each) for each in n_bin_reverse),2)

n = 7
print(bitwiseComplement(n))