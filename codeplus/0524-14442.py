# bfs
# 2206번과 거의 같음
from collections import deque

n, m, k = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
inf = 1e10
d = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y, z = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and d[nx][ny][z] == 0:
                d[nx][ny][z] = d[x][y][z]+1
                q.append((nx, ny, z))
            if z < k and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
                d[nx][ny][z+1] = d[x][y][z]+1
                q.append((nx, ny, z+1))

for i in range(k+1):
    if d[n-1][m-1][i] == 0:
        d[n-1][m-1][i] = inf
ans = min(d[n-1][m-1])
if ans == inf:
    print(-1)
else:
    print(ans)