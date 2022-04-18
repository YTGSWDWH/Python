def findMaxConsecutiveOnes(nums):
    str1 = "".join([str(each) for each in nums])
    list1 = str1.split('0')
    print(list1)
    max = 0
    for each in list1:
        if each.count('1') > max:
            max = each.count('1')
    return max

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))