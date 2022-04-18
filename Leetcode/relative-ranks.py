score = [2,3,1,4,5]
dict1 = {}
list1 = []
list2 = []
for ch,value in enumerate(score):
    dict1[ch] = value
dict1_sort = sorted(dict1.items(), key=lambda x:x[1])
dict1_sort.reverse()
for i in range(len(dict1_sort)):
    list1.append((dict1_sort[i][0], i))
list1.sort()
print(list1)
for i in range(len(list1)):
    if list1[i][1] == 0:
        list2.append('Gold Medal')
    elif list1[i][1] == 1:
        list2.append('Silver Medal')
    elif list1[i][1] == 2:
        list2.append('Bronze Medal')
    else:
        list2.append(str(list1[i][1]))
print(list2)