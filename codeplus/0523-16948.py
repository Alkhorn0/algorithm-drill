# bfs
from collections import deque

n = int(input())
r_1, c_1, r_2, c_2 = map(int, input().split())
d = [[-1]*n for _ in range(n)]
d[r_1][c_1] = 0
q = deque()
q.append((r_1, c_1))

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
while q:
    x, y = q.popleft()
    for k in range(6):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
print(d[r_2][c_2])