import collections
def findErrorNums(nums):
    list1 = []
    set1 = set([each for each in range(1,len(nums)+1)]) - set(nums)
    print(set1)
    for each in set1:
        list1.append(each)
    print(list1)
    count1 = collections.Counter(nums)
    dict1 = dict(count1)
    print(dict1)
    dict2 = sorted(dict1.items(),key=lambda x:x[1],reverse=True)
    print(dict2[0][0])


nums = [1,2,2,4]
dict3 = {i:nums.count(i) for i in range(1,len(nums)+1)}
print(dict3)
findErrorNums(nums)