res_list = []

def isHappy(n):
    if n == 1:
        return True
    res = 0
    for each in str(n):
        res += int(each)**2
    if res in res_list:
        return False
    else:
        res_list.append(res)
    print(res_list)
    return isHappy(res)
    
n = 19
print(isHappy(n))