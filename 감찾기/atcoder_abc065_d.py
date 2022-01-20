from heapq import heapify, heappop, heappush

n = int(input())
x = [0]*n
y = [0]*n

for i in range(n):
    x[i], y[i] = map(int, input().split())

sort_x = sorted(range(n), key=lambda i: x[i])
sort_y = sorted(range(n), key=lambda i: y[i])

cost = [[] for _ in range(n)]
for i in range(n-1):
    j1, j2 = sort_x[i], sort_x[i+1]
    c = abs(x[j1]-x[j2])
    cost[j1].append((c, j2))
    cost[j2].append((c, j1))

    j1, j2 = sort_y[i], sort_y[i+1]
    c = abs(y[j1]-y[j2])
    cost[j1].append((c, j2))
    cost[j2].append((c, j1))

used = [0]*n
used[0] = 1
que = [(c, w) for c, w in cost[0]]

heapify(que)

ans = 0
while que:
    cv, v = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for c, w in cost[v]:
        if used[w]:
            continue
        heappush(que, (c, w))

print(ans)