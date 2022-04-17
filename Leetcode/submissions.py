import collections
def minimumRounds(tasks):
    res = 0
    collect1 = collections.Counter(tasks)
    print(collect1)
    for value in sorted(collect1.values()):
        for i in range(value // 2 + 1):
            for j in range(value // 3 + 1):
                if 2*i + 3*j == value:
                    res += i + j
                    print(value,i,j)
                    break
            else:
                continue
            break
        else:
            return -1

    return res

tasks = [66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]
print(minimumRounds(tasks))