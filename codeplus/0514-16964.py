# 다시보기
n = int(input())
a = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)
b = list(map(int, input().split()))
b = [x-1 for x in b]
order = [0]*n
for i in range(n):
    order[b[i]] = i
for i in range(n):
    a[i].sort(key=lambda x : order[x])

dfs_order = []
visited = [False]*n

def dfs(x):
    if visited[x]:
        return
    dfs_order.append(x)
    visited[x] = True
    for y in a[x]:
        dfs(y)
dfs(0) 

ok = True
for i in range(n):
    if dfs_order[i] != b[i]:
        ok = False
print(1 if ok else 0)