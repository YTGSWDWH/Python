def isLongPressedName(name, typed):
    left = 0
    right = 0
    while left < len(name) and right < len(typed):
        print(left,right,name[left],typed[right])
        if name[left] == typed[right]:
            left += 1
            right += 1
        elif typed[right] == typed[right-1]:
            right += 1
        else:
            return False
    return True

name = "vtkgn"
typed = "vttkgnn"
print(isLongPressedName(name,typed))