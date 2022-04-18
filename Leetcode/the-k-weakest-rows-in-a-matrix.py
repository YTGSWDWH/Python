list1 = [[1,1,0,0,0],
         [1,1,1,1,0],
         [1,0,0,0,0],
         [1,1,0,0.0],
         [1,1,1,1,1]]
list2 = []
k = 3
dict1 = dict(enumerate(list1))
print(dict1)
dict2 = {k1: list1[k1].count(1) for k1 in range(len(dict1))}
print(dict2)
dict3 = sorted(dict2.items(), key=lambda x:x[1])
print(dict3)
for i in range(k):
    list2.append(dict3[i][0])
print(list2)