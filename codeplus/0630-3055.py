# sw 역량 테스트 준비 - 기초 
from collections import deque

r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
w = [[-1]*c for _ in range(r)]
d = [[-1]*c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
e_x, e_y = 0, 0
q_w = deque()
q_d = deque()
for i in range(r):
    for j in range(c):
        if a[i][j] == '*':
           q_w.append((i, j))
           w[i][j] = 0
        if a[i][j] == 'S':
            q_d.append((i, j))
            d[i][j] = 0
        if a[i][j] == 'D':
            e_x = i
            e_y = j

while q_w:
    x, y = q_w.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if w[nx][ny] != -1:
                continue
            if a[nx][ny] == 'D' or a[nx][ny] == 'X':
                continue
            q_w.append((nx, ny))
            w[nx][ny] = w[x][y]+1

while q_d:
    x, y = q_d.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if d[nx][ny] != -1:
                continue
            if a[nx][ny] == 'X':
                continue
            if w[nx][ny] <= d[x][y]+1 and w[nx][ny] != -1:
                continue
            q_d.append((nx, ny))
            d[nx][ny] = d[x][y]+1

print(d[e_x][e_y] if d[e_x][e_y] != -1 else 'KAKTUS')