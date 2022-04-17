def fairCandySwap(aliceSizes, bobSizes):
    list1 = []
    diff = sum(aliceSizes) - sum(bobSizes)
    print(diff)
    for a_each in aliceSizes:
        for b_each in bobSizes:
            if a_each - b_each == diff // 2:
                list1 = [a_each,b_each]
                break
    return list1

A = [1,2,5]
B = [2,4]
print(fairCandySwap(A,B))