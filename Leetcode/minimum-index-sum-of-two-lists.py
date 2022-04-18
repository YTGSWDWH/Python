# def findRestaurant(list1, list2):

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
dict1 = {x:list1.index(x)+list2.index(y) for x in list1 for y in list2 if x == y}
print(dict1)
dict2 = sorted(dict1.items(), key = lambda x:x[1], reverse=False)
print(dict2)
list3 = [each[0] for each in dict2 if each[1] == dict2[0][1]]
print(list3)