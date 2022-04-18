def isPerfectSquare(num):
    for i in range(num):
        if i * i == num:
            return True
        elif i * i > num:
            return False

num = 16
print(isPerfectSquare(num))