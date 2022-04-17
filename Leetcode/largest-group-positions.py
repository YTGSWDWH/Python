s = "bababbaaab"
left = 0
right = 0
list1 = []

while right < len(s)-1:
    if s[left] == s[right]:
        right = right + 1
        print(left,right)
        if right == len(s)-1 and s[right] == s[left]:
            if right - left >= 2:
                list1.append([left,right])
        if right == len(s)-1 and s[right] != s[left]:
            if right - left >= 3:
                list1.append([left,right-1
                
                
                
                
                
                ])
    else:
        if right - left >= 3:
            list1.append([left,right-1])
        left = right

print(list1)