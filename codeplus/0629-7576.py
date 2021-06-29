# sw 역량 테스트 준비 - 기초 
from collections import deque

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1]*m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append((i, j))
            d[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

ans = -1
for i in range(n):
    for j in range(m):
        if a[i][j] != -1:
            ans = max(d[i][j], ans)
            if d[i][j] == -1:
                print(-1)
                exit()
print(ans)
            