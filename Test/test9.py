import sys
line1 = sys.stdin.readline().strip('\n')
line2 = sys.stdin.readline().strip('\n')
line3 = sys.stdin.readline().strip('\n')
input1 = line1
input2 = line2.split()
input3 = line3.split()

input1 = int(input1)
input2 = [int(each) for each in input2]
input3 = [int(each) for each in input3]
input3.sort()

count = 0
for i in range(input1-1):
    if input2[i] != 0:
        input2[i+1] = 1
        count += input3[i+1] - input3[i]
print(count)