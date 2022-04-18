def isMatch(a, b):
    if a == "(" and b == ")" or a == "[" and b == "]" or a == "{" and b == "}":
        return True
    else:
        return False

s = "()["
list1 = []
ans = True
for each in s:
    if each == "(" or each == "[" or each == "{":
        list1.append(each)
    elif len(list1) != 0 and (each == ")" or each == "]" or each == "}"):
        list_pop = list1.pop()
        if  not isMatch(list_pop, each):
            ans = False
    else:
        ans = False
if len(list1) != 0:
    ans = False
print(ans)