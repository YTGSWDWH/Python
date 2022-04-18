def largestSumAfterKNegations(nums,k):
    negative_count = 0
    for each in nums:
        if each < 0:
            negative_count += 1

    if negative_count == 0:
        if k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - min(nums)*2


    elif negative_count < k:
        min1 = min(each for each in nums if each >= 0)
        if (k - negative_count) % 2 == 0:
            return sum(abs(each) for each in nums)
        elif sum(abs(each) for each in nums if each < 0) > min1:
            return sum(abs(each) for each in nums) - min1*2
        else:
            return sum(abs(each) for each in nums) + max(each for each in nums if each < 0)*2
    else:
        count2 = 0
        list2 = [each for each in nums]
        for i in range(k):
            count2 += min(list2)
            list2.remove(min(list2))
            print(count2)
            print(list2)
        return sum(nums) - count2*2

nums = [-8,3,-5,-3,-5,-2]
k = 6
print(largestSumAfterKNegations(nums,k))