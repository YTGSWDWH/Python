s = "A man, a plan, a canal: Panama"

list1 = []
for each in s:
    if each.isalnum():
        list1.append(each)
str1 = "".join(str(each) for each in list1)
str2 = str1.lower()
if str2[::-1] == str2:
    print(True)
else:
    print(False)