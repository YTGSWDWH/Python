import sys
import collections
line1 = sys.stdin.readline().strip('\n')
line2 = sys.stdin.readline().strip('\n')
input1 = int(line1)
input2 = line2.split()

collec = collections.Counter(input2)
count = 0
for each in collec.values():
    if each % 2 == 1:
        count += 1
print(count)