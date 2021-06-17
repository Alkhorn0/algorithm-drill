# 17141번과 유사하지만, 약간 다름
# 바이러스는 활성과 비활성으로 나뉨 -> 비활성이어도 빈칸이 아님
# 빈칸에 퍼지는 최소시간을 구할때 비활성인 바이러스가 배치된 칸은
# 포함 되지 않아야 함
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        # 차이점 1 -> 바이러스가 배치될 후보 좌표는 빈칸이 아님
        # 좌표는 기록하되, 빈칸으로 바꾸지 않음
        if a[i][j] == 2:
            virus.append((i, j))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = -1

def bfs():
    d = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 3:
                q.append((i, j))
                d[i][j] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] != 1 and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
    # 차이점 3 -> 빈 칸에 바이러스가 퍼지는 최소시간을 구함
    # 비활성 바이러스가 배치된 칸은 제외 
    cur = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    if ans == -1 or ans > cur:
        ans = cur

def go(index, cnt):
    if index == len(virus):
        if cnt == m:
            bfs()
    else:
        # 차이점 2 -> 차이점 1과 같이, 
        # 바이러스가 비활성이더라도 빈칸이 아님
        x, y = virus[index]
        # 활성바이러스의 경우 17141문제의 바이러스 배치와 같음
        a[x][y] = 3
        go(index+1, cnt+1)
        # 때문에 빈칸(a[x][y] = 0)이 아닌 2로 남겨둠
        a[x][y] = 2
        go(index+1, cnt)
go(0, 0)
print(ans)