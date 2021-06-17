from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 바이러스를 둘 수 있는 후보 위치 저장
virus = []
ans = -1
for i in range(n):
    for j in range(n):
        # 위치를 파악한 뒤엔 빈 칸 처리
        # (배치 하지 않는 경우 빈칸이기 때문)
        if a[i][j] == 2:
            a[i][j] = 0
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    # 각 칸에 바이러스가 퍼지는 데 걸리는 최소시간 저장
    d = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            # 바이러스가 배치될 후보좌표중 
            # 바이러스가 배치된 좌표의 경우- > 큐에 추가
            if a[i][j] == 3:
                q.append((i, j))
                d[i][j] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                # 벽이 아니고 방문 한 적없는 경우 바이러스 퍼짐
                if a[nx][ny] != 1 and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y]+1
                    q.append((nx, ny))
    cur = 0
    for i in range(n):
        for j in range(n):
            # 벽인 곳을 제외한 모든 곳 중
            # 바이러스가 가장 늦게 퍼진 곳의 값 저장(cur)
            if a[i][j] != 1:
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    # cur값중 가장 작은 값 ans에 저장
    global ans
    if ans == -1 or ans > cur:
        ans = cur

# 바이러스는 m개미만의 칸에 배치 되도 되지만,
# 가장 빠르게 바이러스가 퍼지기위해선 최대한 많이
# 바이러스를 배치하는게 유리한 것은 자명 -> 
# 때문에 m개미만으로 배치하는 경우는 고려할 필요 없음
def go(index, cnt):
    if index == len(virus):
        # 바이러스를 m개 모두 배치한 경우만 bfs진행
        if cnt == m:
            bfs()
    else:
        # 바이러스를 배치할 수 있는 좌표들 중
        # 선택받는 경우와 선택받지 못하는 좌표로 나뉨
        x, y = virus[index]
        # 선택받는 경우
        a[x][y] = 3
        go(index+1, cnt+1)
        # 선택받지 못하는 경우
        a[x][y] = 0
        go(index+1, cnt)

go(0, 0)
print(ans)