import sys
line1 = sys.stdin.readline().strip()

n = len(line1)
fast = slow = 0
max1 = 0
while fast < n-1:
    if line1[fast].isdigit() and line1[fast+1].isdigit() and int(line1[fast+1]) >= int(line1[fast]):
        fast = fast + 1
        max1 = max(max1, fast - slow + 1)
    else:
        fast = fast + 1
        slow = fast
print(max1)