# 다시보기
from collections import deque

w, h = map(int, input().split())
a = [input() for _ in range(h)]
sx = sy = ex = ey = -1
for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if sx == -1:
                sx = i
                sy = j
            else:
                ex = i
                ey = j
d = [[-1]*w for _ in range(h)]
q = deque()
d[sx][sy] = 0
q.append((sx, sy))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        while 0 <= nx < h and 0 <= ny < w:
            if a[nx][ny] == '*':
                break
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
            nx += dx[k]
            ny += dy[k]

print(d[ex][ey]-1)
print(d)