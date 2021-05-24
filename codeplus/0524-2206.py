# 다시보기
# bfs
# 한번만 벽을 부수고 지나갈 수 있음 
# ->어느 칸에 방문시 벽을 부순 경우와 부수지 않은 경우로 나뉨
# -> 때문에 d는 3차원 배열(좌표:2, 벽을 부순 여부: 1)
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
d = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        # 지도 범위 내에 있는 지 확인
        if 0 <= nx < n and 0 <= ny < m:
            # 향한 곳이 원래 빈칸이면 그냥 받음(일반 미로문제는 여기서 끝)
            if a[nx][ny] == 0 and d[nx][ny][z] == 0:
                d[nx][ny][z] = d[x][y][z] + 1
                q.append((nx, ny, z))
            # 향한 곳이 벽인경우에는 이전에 벽을 부쉈는지 여부또한 확인 후 
            # 부수고 가는 행렬의 칸에 추가
            if z == 0 and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
                d[nx][ny][z+1] = d[x][y][z] + 1
                q.append((nx, ny, z+1))
# 결과 표시(목적지의 상태에 따라 분류)

# 목적지에 이르기까지 벽을 부수지 않고도 오는 경우 
# & 벽을 한번 부수고 온 경우 -> 둘 중 더 작은 값
if d[n-1][m-1][0] != 0 and d[n-1][m-1][1] != 0:
    print(min(d[n-1][m-1]))
# 벽을 부수지 않고 오는 경우만 있으면 그대로 출력
elif d[n-1][m-1][0] != 0:
    print(d[n-1][m-1][0])
# 벽을 한번 부숴야지만 올 수 있는 경우 그대로 결과 출력
elif d[n-1][m-1][1] != 0:
    print(d[n-1][m-1][1])
# 그 외에는 모두 불가
else:
    print(-1)