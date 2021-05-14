# 무조건 다시보기
import sys
sys.setrecursionlimit(1000000)
from collections import deque
n = int(input())
a = [[] for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)
# 값의 의미: 0 -> 방문 안함, 1 -> 방문함, 2 -> 사이클에 포함
visited = [0]*n
# -2 -> 사이클 찾음, 포함 안됨
# -1 -> 사이클 못 찾음
# 0~n-1 -> 사이클 찾음, 사이클의 시작 인덱스나타냄
def go(x, p):
    if visited[x] == 1:
        return x
    visited[x] = 1
    for y in a[x]:
        if y == p:
            continue
        res = go(y, x)
        if res == -2:
            return -2
        if res >= 0:
            visited[x] = 2
            if x == res:
                return -2
            else:
                return res
    return -1

go(0, -1)
q = deque()
dist = [-1]*n
for i in range(n):
    if visited[i] == 2:
        dist[i] = 0
        q.append(i)
    else:
        dist[i] = -1

while q:
    x = q.popleft()
    for y in a[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x]+1
        
print(*dist, sep = ' ')