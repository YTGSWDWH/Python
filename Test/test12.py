import sys
line1 = sys.stdin.readline().strip('\n')
line2 = sys.stdin.readline().strip('\n')
input1 = int(line1)
input2 = line2.split()

list1 = [int(each) for each in input2]
list1.sort()
print(list1)
max_count = 0
for i in range(input1):
    for j in range(i+1,input1):
        count = 0
        times = 1
        for k in range(j+1,input1):
            if list1[k] / list1[j] == (list1[j] / list1[i])**times:
                count += 1
                times += 1
        max_count = max(max_count,count)
        print(i,j,k,max_count)
print(max_count+2)