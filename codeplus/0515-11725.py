# 트리, bfs, parent 주목
from collections import deque

n = int(input())
a = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0]*(n+1)
q = deque()
for _ in range(n-1):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
q.append(1)
visited[1] = True
while q:
    x = q.popleft()
    for i in a[x]:
        if not visited[i]:
            visited[i] = True
            parent[i] = x
            q.append(i)

for j in range(2, n+1):
    print(parent[j])