def isValid(s):
    stack = []
    kohaomap = {"}":"{","]":"[",")":"("}
    for i in s:
        if i not in kohaomap:
            stack.append(i)
        elif not stack or kohaomap[i] != stack.pop():
            return False
    return not stack

s = "{]"
print(isValid(s))