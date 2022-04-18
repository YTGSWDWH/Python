import sys
line1 = sys.stdin.readline().strip('\n')
line2 = sys.stdin.readline().strip('\n')
input1 = line1.split()
x = int(input1[0]) - (line2.count('E') - line2.count('W'))
y = int(input1[1]) - (line2.count('S') - line2.count('N'))
z = int(input1[2]) - (line2.count('U') - line2.count('D'))
print(str(x) + ' ' + str(y) + ' ' + str(z))