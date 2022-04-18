import math
def constructRectangle(area):
    list1 = []
    a = math.ceil(area ** 0.5)
    for i in range(a, area+1):
        if area % i == 0:
            list1.append(i)
            list1.append(area//i)
            break
    return list1

area = 2
print(constructRectangle(area))