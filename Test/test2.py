nums = ["5,3,4,2,3","1,5,2,2,3","3,2,5,2,1","1,4,2,5,2","1,2,3,1,5"]

list2 = []
for i in range(len(nums)):
    list1 = nums[i].split(',')
    list3 = [int(each) for each in list1]
    list2.append(list3)
Transpose = [[row[i] for row in list2] for i in range(5)]
print(Transpose)
dict1 = {i:sum(Transpose[i])-5 for i in range(5)}
dict2 = sorted(dict1.items(), key = lambda x:(-x[1], x[0]))
# dict2 = sorted(dict1.items(), key = lambda x:x[1], reverse=True)
print(dict2)
print(dict2[0][0])
