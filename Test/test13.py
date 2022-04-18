import sys
input1 = sys.stdin.readline().strip('\n')
n = len(input1)

list1 = []
for i in range(n):
    if input1[i] != '[' and input1[i] != ']' and input1[i] != ',':
        list1.append(int(input1[i]))
    if input1[i] == ']':
        break
list2 = []
for j in range(i+2,n):
    if input1[j] != '[' and input1[j] != ']' and input1[j] != ',':
        list2.append(int(input1[j]))
    if input1[j] == ']':
        break

list3 = list1 + list2
list3.sort()
n = len(list3)
if n % 2 == 1:
    print(list3[n//2])
else:
    print((list3[n//2-1] + list3[n//2]) / 2)