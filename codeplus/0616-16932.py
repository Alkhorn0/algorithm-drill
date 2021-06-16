# bfs
# 모든칸을 바꾸며 진행하는 것은 시간초과가 됨 -> bfs를 먼저 사용하여 그룹의 크기를 먼저 구함
# 이후 a[i][j] = 0 인 칸만 바꿔보며 확인한다
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 그룹분할 현황
group = [[0]*m for _ in range(n)]
# 그룹의 크기 저장 (ex> 1번그룹의 크기 = 3 & 2번그룹의 크기 = 4)
group_size = [0]
# 좌표가 포함되는 그룹의 번호
groupn = 0

# 주어진 행렬의 그룹화를 위해 사용
def bfs(sx, sy):
    # 그룹의 번호
    global groupn
    # 1번 그룹부터 시작
    groupn += 1
    q = deque()
    q.append((sx, sy))
    group[sx][sy] = groupn
    cnt = 1
    while q:
        x, y = q.popleft()
        # 인접하는 좌표가 있는경우 같은 그룹으로 묶인다 => group[x][y] = group[nx][ny] = groupn
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if group[nx][ny] == 0 and a[nx][ny] == 1:
                    group[nx][ny] = groupn
                    q.append((nx, ny))
                    # 그룹의 크기 세줌
                    cnt += 1
    group_size.append(cnt)

# 우선적으로 그룹화
for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and group[i][j] == 0:
            bfs(i, j)

# a[i][j] = 0 인곳만 1로 바꿔가며 확인
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            near = set()
            # 고른 좌표에 인접하는 그룹이 있다면 좌표를 그 그룹에 포함시켜준다
            # 단 같은 그룹이 여러번 포함되지 않기 위해 set을 사용
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 1:
                        near.add(group[nx][ny])
            # 선택한 좌표가 포함되면서 원래 그룹의 크기에 1이 더해진다
            s = 1
            # 선택한 좌표를 통해 여러 그룹이 이어질 수 있기 때문에 집합near의 요소인
            # neighbor(선택한 좌표에 인접한 그룹번호)의 그룹크기를 더해준다. 
            for neighbor in near:
                s += group_size[neighbor]
            if ans < s:
                ans = s
print(ans)