# sw 역량 테스트 준비 - 기초 
from collections import deque

n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(v)
print()

visited = [False]*(n+1)
q = deque()
q.append(v)
visited[v] = True
while q:
    x = q.popleft()
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            q.append(i)
            visited[i] = True