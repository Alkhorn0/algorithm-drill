n, m = map(int, input().split())
g = [[False]*(n+1) for _ in range(n+1)]
a = [0]*m
b = [0]*m
for i in range(m):
    a_i, b_i = map(int, input().split())
    g[a_i][b_i] = True
    g[b_i][a_i] = True
    a[i] = a_i
    b[i] = b_i

def dfs(v):
    visited[v] = True
    for i in range(n+1):
        if g[v][i] == True:
            if not visited[i]:
                dfs(i)
    if False in visited[1:]:
        return True
    else:
        return False
ans = 0
for i in range(m):
    visited = [False]*(n+1)
    g[a[i]][b[i]] = False
    g[b[i]][a[i]] = False
    if dfs(1):
        ans += 1
    g[a[i]][b[i]] = True
    g[b[i]][a[i]] = True
print(ans)
    