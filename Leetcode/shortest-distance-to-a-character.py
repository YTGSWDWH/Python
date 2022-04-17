def shortestToChar(S, C):
    prev = float('-inf')
    ans = []
    for i, x in enumerate(S):
        if x == C: prev = i
        ans.append(i - prev)
        print(ans)
    prev = float('inf')
    for i in range(len(S) - 1, -1, -1):
        if S[i] == C: prev = i
        ans[i] = min(ans[i], prev - i)

    return ans

s = "loveleetcode"
c = "e"
print(shortestToChar(s,c))