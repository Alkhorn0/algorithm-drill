# bfs, 최단거리?
from collections import deque

n, k = map(int, input().split())
visited = [0]*100001
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        print(visited[x])
        break
    for i in [x-1, x+1, 2*x]:
        if 0 <= i <= 100000 and not visited[i]:
            q.append(i)
            visited[i] = visited[x]+1