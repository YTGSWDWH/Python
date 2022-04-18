import collections

def interchangeableRectangles(rectangles):
    list1 = [rectangle[0]/rectangle[1] for rectangle in rectangles]
    print(list1)
    # dict1 = {each:list1.count(each) for each in list1}
    dict1 = dict(collections.Counter(list1))
    print(dict1)
    count1 = 0
    for _,value in dict1.items():
        if value >= 2:
            count1 = count1 + value*(value-1)//2
    print(count1)
rectangles = [[4,8],[3,6],[10,20],[15,30]]
interchangeableRectangles(rectangles)