# 다시보기
# 레이저는 중간에 장애물이 없는 이상 그대로 직진
# 시작점에서 도착점까지 거친 직선의 갯수 - 1 
# = 직선이 꺾인 횟수 = 거울의 갯수
from collections import deque

w, h = map(int, input().split())
a = [input() for _ in range(h)]
# 시작위치와 끝나는 위치를 받음
sx = sy = ex = ey = -1
for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if sx == -1:
                sx = i
                sy = j
            else:
                ex = i
                ey = j

# 메모이제이션을 할 배열 생성 
# (시작점에서 그 정점에 도착하기 까지 거친 직선의 갯수 기록)
d = [[-1]*w for _ in range(h)]
q = deque()
d[sx][sy] = 0
q.append((sx, sy))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for k in range(4):
        # 나아갈 방향 결정
        nx, ny = x+dx[k], y+dy[k]
        # 지도의 끝에 도착할때까지 연장(직선)
        while 0 <= nx < h and 0 <= ny < w:
            # 벽에 도착시 거기서 종료
            if a[nx][ny] == '*':
                break
            # 방문한 적 없으면 숫자 대입
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                # 포함하는 열 또는 행 전부 queue에 추가
                q.append((nx, ny))
            # 결정한 방향의 직선
            nx += dx[k]
            ny += dy[k]
# 거울의 갯수 = 거쳐간 직선의 갯수 - 1
print(d[ex][ey]-1)