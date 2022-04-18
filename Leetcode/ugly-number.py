def isUgly(n):
    if n == 1:
        return True
    else:
        while(n != 0):
            if n == 2 or n == 3 or n == 5:
                return True
            elif n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False

n = 14
print(isUgly(n))
list1 = [1,2,3]
list2 = [1,2]
print(list1 - list2)