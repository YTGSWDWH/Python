def calPoints(ops):
    list1 = []
    for i in range(len(ops)):
        if ops[i].lstrip('-').isdigit():
            list1.append(int(ops[i]))
        elif ops[i] == "C":
            list1.pop()
        elif ops[i] == "D":
            list1.append(list1[-1]*2)
        elif ops[i] == "+":
            list1.append(list1[-1]+list1[-2])
        print(list1)

ops = ["5","-2","4","C","D","9","+","+"]
calPoints(ops)