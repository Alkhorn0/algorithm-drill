from collections import deque

n = int(input())
g = list([] for _ in range(n+1))
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(s):
    dist = [-1]*(n+1)
    q = deque([s])
    dist[s] = 0

    while q:
        v = q.popleft()
        for i in g[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                q.append(i)
    return dist

fennec = bfs(1)
snuke = bfs(n)

cnt = 0
for i in range(1, n+1):
    if fennec[i] <= snuke[i]:
        cnt += 1
if cnt > n-cnt:
    print('Fennec')
else:
    print('Snuke')