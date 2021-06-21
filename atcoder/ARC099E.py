# 다시보기
from collections import deque
n,m = map(int,input().split())
e = [[0]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a][b] = e[b][a] = 1
 
g = [[] for i in range(n)]
vis = [0]*n
for i in range(n):
    for j in range(i):
        if e[i][j]:
            continue
        g[i].append(j)
        g[j].append(i)
 
A = []
B = []
for i in range(n):
    if vis[i]:
        continue
    q = deque([i])
    dis = [-1]*n
    dis[i] = 0
    while q:
        now = q.popleft()
        for nex in g[now]:
            if dis[nex] == dis[now]:
                print(-1)
                exit()
            if dis[nex] == -1:
                dis[nex] = dis[now]^1
                q.append(nex)
                
    a = 0
    b = 0
    for i in range(n):
        if dis[i] == -1:
            continue
        vis[i] = 1
        if dis[i] == 0:
            a += 1
        else:
            b += 1
    A.append(a)
    B.append(b)
 
dp = [0]*(n+1)
dp[0] = 1
 
for a,b in zip(A,B):
 
    ndp = [0]*(n+1)
    for i in range(n+1):
        if dp[i]:
            ndp[i+a] = 1
            ndp[i+b] = 1
    dp = ndp
 
ans = 10**10
 
for i in range(n+1):
    if dp[i] == 0:
        continue
    a = i
    b = n-a
    ans = min(ans,a*(a-1)//2+b*(b-1)//2)
print(ans)