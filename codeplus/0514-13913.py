# 다시보기
from collections import deque
import sys
sys.setrecursionlimit(200000)
visited = [False]*100001
dist = [-1]*100001
via = [-1]*100001
n, k = map(int, input().split())
visited[n] = True
dist[n] = 0
q = deque()
q.append(n)
while q:
    x = q.popleft()
    for i in [x-1, x+1, 2*x]:
        if 0<= i <= 100000 and not visited[i]:
            q.append(i)
            visited[i] = True
            dist[i] = dist[x]+1
            via[i] = x
print(dist[k])
def go(n, k):
    if n != k:
        go(n, via[k])
    print(k, end=' ')
go(n, k)