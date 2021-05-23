# bfs, recursion
from collections import deque
import sys
sys.setrecursionlimit(200000)
n, k = map(int, input().split())
visited = [False]*100001
dist = [0]*100001
via = [0]*100001
q = deque()
q.append(n)
visited[n] = True

while q:
    x = q.popleft()
    for i in [2*x, x+1, x-1]:
        if 0 <= i <= 100000 and not visited[i]:
            q.append(i)
            dist[i] = dist[x]+1
            via[i] = x
            visited[i] = True
print(dist[k])

def go(n, k):
    if n != k:
        go(n, via[k])
    print(k, end=' ')
go(n, k)