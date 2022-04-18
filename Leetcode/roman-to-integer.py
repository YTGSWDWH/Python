x = "MCMXCIV"
ans = 0
for i in range(len(x)):
    if(x[i] == "I"):
        if(i == len(x) - 1):
            ans = ans + 1
        elif(x[i+1] != "V" and x[i+1] != "X"):
            ans = ans + 1
        else:
            ans = ans - 1
    elif(x[i] == "V"):
        ans = ans + 5
    elif(x[i] == "X"):
        if(i == len(x) - 1):
            ans = ans + 10
        elif(x[i+1] != "L" and x[i+1] != "C"):
            ans = ans + 10
        else:
            ans = ans - 10
    elif(x[i] == "L"):
        ans = ans + 50
    elif(x[i] == "C"):
        if(i == len(x) - 1):
            ans = ans + 100
        elif(x[i+1] != "D" and x[i+1] != "M"):
            ans = ans + 100
        else:
            ans = ans - 100
    elif(x[i] == "D"):
        ans = ans + 500
    elif(x[i] == "M"):
        ans = ans + 1000
print(ans)