# bfs
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0
while q:
    x, y = q.popleft()
    for k in range(8):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
ans = -1
for i in range(n):
    for j in range(m):
        if ans < dist[i][j]:
            ans = dist[i][j]
print(ans)