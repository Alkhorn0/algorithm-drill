# 다시보기
# 벽 주변의 이동가능한 빈칸을 그룹화하여 벽인 정점을 기준으로 
# 4방향중에 인접한 그룹에 포함한 정점의 갯수를 더해줌으로서 풀 수 있다
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
# 빈칸인 정점의 그룹을 나타내기 위한 배열
group = [[-1]*m for _ in range(n)]
# bfs시 방문 확인
check = [[False]*m for _ in range(n)]
# 그룹에 포함된 정점의 갯수 기록
group_size = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sx, sy):
    # 그룹번호 (0부터 시작)
    g = len(group_size)
    q = deque()
    q.append((sx, sy))
    group[sx][sy] = g
    check[sx][sy] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                # 방문한적 없는 빈칸만 셈
                if check[nx][ny] == False and a[nx][ny] == 0:
                    check[nx][ny] = True
                    group[nx][ny] = g
                    q.append((nx, ny))
                    # 그룹에 포함된 정점의 갯수 
                    cnt += 1
    group_size.append(cnt)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            # 근접한 빈칸이 포함된 그룹번호 추가
            near = set()
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        near.add(group[nx][ny])
            # 기준이 되는 벽의 정점 또한 갯수에 세야함
            ans = 1
            for g in near:
                ans += group_size[g]
            print(ans%10, end='')
    print()