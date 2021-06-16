# bfs
# 참고 벽 부수고 이동하기 2 
# dist에 좌표파라미터 + 나이트 이동한 횟수 파라미터를 추가하여 계산
from collections import deque

k = int(input())
w, h = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
dx = [-1, 1, 0, 0, -1, -2, -2, -1, 1, 2, 1, 2]
dy = [0, 0, -1, 1, -2, -1, 1, 2, 2, 1, -2, -1]
dz = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
dist = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]
q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 0
while q:
    x, y, z = q.popleft()
    for i in range(12):
        nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
        if 0 <= nx < h and 0 <= ny < w:
            if a[nx][ny] == 1:
                continue
            if nz <= k:
                if dist[nx][ny][nz] == -1:
                    dist[nx][ny][nz] = dist[x][y][z]+1
                    q.append((nx, ny, nz))

ans = -1
for i in range(k+1):
    if dist[h-1][w-1][i] == -1:
        continue
    if ans == -1 or ans > dist[h-1][w-1][i]:
        ans = dist[h-1][w-1][i]
print(ans)