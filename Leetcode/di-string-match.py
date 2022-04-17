def diStringMatch(s):
    list1 = [each for each in range(len(s)+1)]
    print(list1)
    for _ in range(2):
        for i in range(len(s)):
            if s[i] == 'I':
                if list1[i] > list1[i+1]:
                    list1[i+1],list1[i] = list1[i],list1[i+1]
            if s[i] == 'D':
                if list1[i] < list1[i+1]:
                    list1[i+1],list1[i] = list1[i],list1[i+1]
            print(list1)

s = "DDI"
diStringMatch(s)