list1 = [0,4,3,0]
target = 0
list2 = []

for i in range(len(list1)):
    if(target-list1[i] in list1 and target-list1[i]!=list1[i]):
        list2.append(i)
    elif(list1[i]==target/2 and list1.count(list1[i])==2):
        list2.append(i)
print(list2)