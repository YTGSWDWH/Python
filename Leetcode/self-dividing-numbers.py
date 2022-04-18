left = 1
right = 22

def baichu(num):
    num1 = num
    while num1 != 0:
        if num1 % 10 == 0:
            return False
        elif num % (num1 % 10) != 0:
            return False
        else:
            num1 = num1 // 10
    return True

list1 = []
for i in range(left,right+1):
    if baichu(i):
        list1.append(i)
print(list1)