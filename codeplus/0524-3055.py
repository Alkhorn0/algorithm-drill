# bfs
# 물의 이동과 고슴도치의 이동에 각각 bfs를 하여 비교하며 진행

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
a = [input() for _ in range(n)]
# 물의 이동
water = [[-1]*m for _ in range(n)]
# 고슴도치의 이동
dist = [[-1]*m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            q.append((i,j))
            water[i][j] = 0
        elif a[i][j] == 'S':
            sx,sy = i,j
        elif a[i][j] == 'D':
            ex,ey = i,j
while q:
    x,y = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # 한번 방문한 정점은 제외
            if water[nx][ny] != -1:
                continue
            # X-> 벽/ D-> 도착지 에는 물이 가지 않음
            if a[nx][ny] in 'XD':
                continue
            water[nx][ny] = water[x][y] + 1
            q.append((nx,ny))

q.append((sx,sy))
dist[sx][sy] = 0
while q:
    x,y= q.popleft()
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # 방문한 정점 제외
            if dist[nx][ny] != -1:
                continue
            # 벽에는 갈 수 없음
            if a[nx][ny] == 'X':
                continue
            # 배열 water 는 그 위치로 물이 가기 까지 걸린 시간을 의미,
            # 마찬가지로 dist또한 고슴도치가 그 위치에 도착하기 까지 걸린 시간을 의미
            # 때문에 고슴도치가 한 정점에 도착했을때 걸린 시간이 
            # 물이 도착하기까지 걸린 시간보다 크다면 이미 물이 차있는 상태 
            # -> 진행 불가
            if water[nx][ny] != -1 and dist[x][y]+1 >= water[nx][ny]:
                continue
            dist[nx][ny] = dist[x][y]+1
            q.append((nx,ny))

if dist[ex][ey] == -1:
    print('KAKTUS')
else:
    print(dist[ex][ey])
