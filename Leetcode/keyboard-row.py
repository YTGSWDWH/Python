def findWords(words):
    list1 = []
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"
    for each in words:
        if (set(each.lower()) & set(first) == set(each.lower())) or (set(each.lower()) & set(second) == set(each.lower())) or (set(each.lower()) & set(third) == set(each.lower())):
            list1.append(each)
    return list1

words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))