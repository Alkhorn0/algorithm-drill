# 다시보기
n, m = map(int, input().split())
a = [0]*m
b = [0]*m

visited = [False]*(n+1)
graph = [[False]*(n+1) for _ in range(n+1)]

for i in range(m):
    a[i], b[i] = map(int, input().split())
    graph[a[i]][b[i]] = graph[b[i]][a[i]] = True

ans = 0

def dfs(v):
    visited[v] = True
    for v2 in range(1, n+1):
        if graph[v][v2] == False:
            continue
        if visited[v2] == True:
            continue
        dfs(v2)

for i in range(m):
    graph[a[i]][b[i]] = graph[b[i]][a[i]] = False
    for j in range(1, n+1):
        visited[j] = False
    dfs(0)
    birdge = False
    for j in range(1, n+1):
        if visited[j] == False:
            bridge = True
    if bridge:
        ans += 1
    graph[a[i]][b[i]] = graph[b[i]][a[i]] = True

print(ans)