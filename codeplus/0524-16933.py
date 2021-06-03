# 시간초과
# 다시 보기 d
from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
d = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
d[0][0][0] = 1
q = deque()
q.append((0, 0, 0))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
day = True
while q:
    x, y, z = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] == 0 and d[nx][ny][z] == 0:
            d[nx][ny][z] = d[x][y][z]+1
            q.append((nx, ny, z))
        if z < k and a[nx][ny] == 1 and d[nx][ny][z] == 0:
            if day:
                d[nx][ny][z+1] = d[x][y][z] + 1
                q.append((nx, ny, z+1))
            else:
                if (x, y, z) not in q:
                    d[x][y][z] += 1
                    q.append((x, y, z))
    if day:
        day = False
    else:
        day = True

inf = 1e10
for i in range(k+1):
    if d[n-1][m-1][i] == 0:
        d[n-1][m-1][i] = inf
ans = min(d[n-1][m-1])
if ans == inf:
    print(-1)
else:
    print(ans)