# sw 역량 테스트 준비 - 기초 
from collections import deque

m, n = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
d = [[-1]*m for _ in range(n)]
q = deque()
q.append((0, 0))
d[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if d[nx][ny] != -1:
                continue
            if a[nx][ny] == 0:
                d[nx][ny] = d[x][y]
                q.appendleft((nx, ny))
            elif a[nx][ny] == 1:
                d[nx][ny] = d[x][y]+1
                q.append((nx, ny))

print(d[n-1][m-1])