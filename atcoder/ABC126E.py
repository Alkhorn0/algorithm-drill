# dfs, union find
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def dfs(v):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i)

for v in range(1, n+1):
    if not visited[v]:
        ans += 1
        dfs(v)
print(ans)