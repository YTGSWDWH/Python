import collections

paragraph = "Bob"
banned = []

list1 = []
list2 = []
for i in range(len(paragraph)):
    if i == len(paragraph)-1 and paragraph[i].isalpha():
        list1.append(paragraph[i])
        list2.append("".join(each.lower() for each in list1))
    elif paragraph[i].isalpha():
        list1.append(paragraph[i])
    elif not paragraph[i].isalpha() and paragraph[i-1].isalpha():
        list2.append("".join(each.lower() for each in list1))
        list1 = []
print(list2)
dict1 = collections.Counter(list2)
list3 = dict1.most_common(2)
print(list3)
print(list3[0][0])