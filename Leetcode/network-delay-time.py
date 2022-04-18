times = [[1,2,1],[2,3,2],[1,3,4]]
n = 3
k = 1

g = [[float('inf')] * n for _ in range(n)]
print(g)
for x, y, time in times:
    g[x - 1][y - 1] = time

print(g)

dist = [float('inf')] * n
dist[k - 1] = 0
used = [False] * n

for _ in range(n):
    x = -1
    for y, u in enumerate(used):
        if not u and (x == -1 or dist[y] < dist[x]):
            x = y
    used[x] = True
    for y, time in enumerate(g[x]):
        dist[y] = min(dist[y], dist[x] + time)

ans = max(dist)

if ans < float('inf'):
    ans = ans
else:
    ans = -1
print(ans)