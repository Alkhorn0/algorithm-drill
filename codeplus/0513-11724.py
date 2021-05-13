n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(v):
    visited[v] = True
    for i in g[v]:
        if visited[i]:
            continue
        dfs(i)

ans = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)