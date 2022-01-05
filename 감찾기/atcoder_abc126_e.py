import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    x, y, z = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def dfs(v, ans):
    if visited[v] != 0:
        return 
    visited[v] = ans
    for i in g[v]:
        dfs(i, ans)
        visited[i] = ans
ans = 0
for i in range(1, n+1):
    if visited[i] != 0:
        continue
    ans += 1
    dfs(i, ans)
print(max(visited))