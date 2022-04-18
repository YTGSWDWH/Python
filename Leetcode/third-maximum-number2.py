def thirdMax(nums):
    third = float('-inf')
    second = float('-inf')
    first = float('-inf')
    for each in nums:
        if each == first or each == second or each == third:
            pass
        elif each > first:
            third = second
            second = first
            first = each
        elif each > second:
            third = second
            second = each
        elif each > third:
            third = each
        print(first, second,third)
    if third == float('-inf'):
        return first
    else:
        return third

nums = [2,2,3,1]
print(thirdMax(nums))