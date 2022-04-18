nums = [1,2,3,4,5]

if len(nums) == 1:
    max1 = nums[0]
else:
    max1 = float('-inf')
    for i in range(len(nums)):
        for offset in range(len(nums)-i):
            list1 = []
            for number in range(i+1):
                list1.append(nums[number + offset])
            print(list1)
"""             sum1 = sum(list1) 
            if sum1 > max1:
                max1 = sum1
print(max1) """