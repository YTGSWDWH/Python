import collections
def hasGroupsSizeX(deck):
    deck_collection = dict(collections.Counter(deck))
    for i in range(2,len(deck)//2):
        count = 0
        for value in deck_collection.values():
            print(i,value)
            count += 1
            if value % i != 0:
                count -= 1
                break
        print(count)
        if count == len(deck_collection):
            return True
    return False

deck = [1,1]
print(hasGroupsSizeX(deck))