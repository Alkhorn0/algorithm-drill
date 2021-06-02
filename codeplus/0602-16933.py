# 시간초과
from collections import deque
import sys
input = sys.stdin.readline

inf = 1e10

n, m, k = map(int, input().split())
a = [list(input()) for _ in range(n)]
dist = [[[[inf]*2 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0, 0))
dist[0][0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, z, day = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] == '0' and dist[nx][ny][z][1-day] == inf:
            dist[nx][ny][z][1-day] = dist[x][y][z][day]+1
            q.append((nx, ny, z, 1-day))
        if a[nx][ny] == '1' and z < k and dist[nx][ny][z][1-day] == inf:
            if day == 0:
                dist[nx][ny][z+1][1-day] = dist[x][y][z][day]+1
                q.append((nx, ny, z+1, 1-day))
            else:
                if (x, y, z, 1-day) not in q:
                    dist[x][y][z][1-day] = dist[x][y][z][day]+1
                    q.append((x, y, z, 1-day))
        

ans = min(min(dist[n-1][m-1]))
if ans == inf:
    print(-1)
else:
    print(ans)