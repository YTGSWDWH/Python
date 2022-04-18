head = [1,1,2,3,3]

for each in head:
    while head.count(each) != 1:
        head.remove(each)

print(head)