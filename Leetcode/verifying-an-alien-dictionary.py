def isAlienSorted(words, order):
    dict1 = {order[i]:i for i in range(len(order))}
    for i in range(len(words)-1):
        if words[i][0:len(words[i+1])] == words[i+1]:
            return len(words[i]) < len(words[i+1])
        for j in range(min(len(words[i]), len(words[i+1]))):
            print(words[i][j],words[i+1][j])
            if dict1[words[i][j]] < dict1[words[i+1][j]]:
                break
            elif dict1[words[i][j]] > dict1[words[i+1][j]]:
                return False
    return True

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words,order))