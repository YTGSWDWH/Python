import sys
import collections
line1 = sys.stdin.readline().strip('\n')
line2 = sys.stdin.readline().strip('\n')
input1 = line1.split()
input2 = line2

list1 = []
list2 = []

for i in range(int(input2)):
    line2_1 = sys.stdin.readline().strip('\n')
    input2_1 = line2_1.split()
    input2_1 = [int(each) for each in input2_1]
    list1.append(input2_1)

line3 = sys.stdin.readline().strip('\n')
input3 = line3
for i in range(int(input3)):
    line3_1 = sys.stdin.readline().strip('\n')
    input3_1 = line3_1.split()
    input3_1 = [int(each) for each in input3_1]
    list2.append(input3_1)

list3 = [list2[i][0] for i in range(len(list2))]
collec = collections.Counter(list3)