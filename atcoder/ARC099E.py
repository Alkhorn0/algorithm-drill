# 다시보기
from collections import deque

n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = g[b][a] = 1
# 보그래프(원래의 그래프와 연결과 비연결에 대한 정보가 반대인 그래프)
graph = [[] for _ in range(n)]
visited = [0]*n
for i in range(n):
    for j in range(i):
        if g[i][j]:
            continue
        graph[i].append(j)
        graph[j].append(i)

A = []
B = []
for i in range(n):
    if visited[i]:
        continue
    q = deque()
    q.append(i)
    dist = [-1]*n
    dist[i] = 0
    while q:
        x = q.popleft()
        for v in graph[x]:
            # 완전이분그래프가 아닌경우
            if dist[v] == dist[x]:
                print(-1)
                exit()
            if dist[v] == -1:
                dist[v] = dist[x]^1
                q.append(v)
    a = 0
    b = 0
    for i in range(n):
        if dist[i] == -1:
            continue
        visited[i] = 1
        if dist[i] == 0:
            a += 1
        else:
            b += 1
    A.append(a)
    B.append(b)

dp = [0]*(n+1)
dp[0] = 1

for a, b in zip(A, B):
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
    ans = min(ans, a*(a-1)//2 + b*(b+1)//2)
print(ans)