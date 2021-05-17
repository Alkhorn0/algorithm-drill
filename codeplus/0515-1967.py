# 1167번과 같이 볼 것, 트리
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n+1)]
dist = [0]*(n+1)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    a[p].append((c, w))
    a[c].append((p, w))

def bfs(start):
    visited = [False]*(n+1)
    q = deque()
    q.append(start)
    visited[start] = True
    dist[start] = 0
    while q:
        x = q.popleft()
        for e, w in a[x]:
            if not visited[e]:
                dist[e] = dist[x] + w
                q.append(e)
                visited[e] = True

bfs(1)
start = 1
for i in range(2, n+1):
    if dist[start] < dist[i]:
        start = i
bfs(start)
ans = dist[1]
for i in range(2, n+1):
    ans = max(ans, dist[i])

print(ans)