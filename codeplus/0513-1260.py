from collections import deque

n, m, v = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n):
    g[i].sort()

def dfs(v):
    visited[v] = True
    print(v,end=' ')
    for i in g[v]:
        if not(visited[i]):
            dfs(i)

dfs(v)
print()
def bfs(v):
    visited = [False] * (n+1)
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in g[x]:
            if not(visited[i]):
                visited[i] = True
                q.append(i)
bfs(v)