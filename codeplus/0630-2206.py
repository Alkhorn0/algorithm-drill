# sw 역량 테스트 준비 - 기초 
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
d = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and d[nx][ny][z] == 0:
                d[nx][ny][z] = d[x][y][z] + 1
                q.append((nx, ny, z))
            elif a[nx][ny] == 1 and z == 0 and d[nx][ny][z+1] == 0:
                d[nx][ny][z+1] = d[x][y][z] + 1
                q.append((nx, ny, z+1))

if 0 in d[n-1][m-1]:
    print(max(d[n-1][m-1]) if max(d[n-1][m-1]) != 0 else -1)
else:
    print(min(d[n-1][m-1]))