def checkPerfectNumber(num):
    list1 = [1]
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            list1.append(i)
            if i**2 != num:
                list1.append(num//i)
    return list1

num = 16
print(checkPerfectNumber(num))