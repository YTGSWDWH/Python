# names = ["王飞","刘洋","李丽"]
# scores = ["89,92,95,88,91","92,96,81,90,92","89,91,91,78,97"]
# list1 = []
# list4 = []
# for i in range(3):
#     list2 = scores[i].split(',')
#     list3 = [int(each) for each in list2]
#     list1.append(sum(list3))
# dict1 = dict(zip(names,list1))
# dict2 = sorted(dict1.items(),key=lambda x:x[1])
# for i in range(3):
#     list4.append(dict2[i][0])

# print(list1)
# print(dict2)
# print(list4)

def x(names,scores):
    list1 = []
    list4 = []
    for i in range(3):
        list2 = scores[i].split(',')
        list3 = [int(each) for each in list2]
        list1.append(sum(list3))
    dict1 = dict(zip(names,list1))
    dict2 = sorted(dict1.items(),key=lambda x:x[1],reverse=True)
    for j in range(3):
        list4.append(dict2[j][0])
    return list4

names = ["王飞","刘洋","李丽"]
scores = ["89,92,95,88,91","92,96,81,90,92","89,91,91,78,97"]
print(x(names,scores))