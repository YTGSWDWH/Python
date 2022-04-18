def canThreePartsEqualSum(arr):
    one_third = sum(arr) / 3
    print(one_third)
    count1 = 0
    count2 = 0
    count3 = 0
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        count1 += arr[i]
        if count1 == one_third:
            left = i
            break
    for i in range(len(arr)):
        count2 += arr[-1-i]
        if count2 == one_third:
            right = len(arr)-1 - i
            break
    if left+1 < right:
        for i in range(left+1,right):
            count3 += arr[i]
        if count3 == one_third:
            return True
        else:
            return False
    else:
        return False
    
arr = [0,2,1,-6,6,-7,9,1,2,0,1]
print(canThreePartsEqualSum(arr))