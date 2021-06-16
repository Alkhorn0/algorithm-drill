# 다시보기
# 거울(문도 거울로 취급)에 번호를 매겨 몇번 거울을 거쳐 도착점에 도착하는 지 판단
# 즉, 거울의 좌표로 bfs를 해나간다.

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())
# 입력받은 집의 상태
s = [input() for _ in range(n)]
# 몇 개의 거울을 거쳐 보일 수 있는지 저장
b = [[0]*n for _ in range(n)]
v = []
# 시작점인 문과 도착점인 문을 거울이라 하고 번호를 매겼을때 그 번호 저장
start, end = -1, -1
for i in range(n):
    for j in range(n):
        if s[i][j] == '#':
            if start == -1:
                start = len(v)
            else:
                end = len(v)
            v.append((i, j))
            b[i][j] = len(v) - 1
        elif s[i][j] == '!':
            v.append((i, j))
            b[i][j] = len(v) - 1
# 거울의 개수 + 2(문2개)
m = len(v)
# 거울에 순서를 매겨 서로 연장선상에 존재하는 지 여부 판단
a = [[False]*m for _ in range(m)]
for i in range(len(v)):
    # 같은 방향의 직선상의 칸은 전부 보임(체스의 룩의 이동방향)
    for k in range(4):
        x, y = v[i]
        x += dx[k]
        y += dy[k]
        while 0 <= x < n and 0 <= y < n:
            # 벽으로 막혀있으면 안됨
            if s[x][y] == '*':
                break
            # 거울이나 문의 경우 연장선상에 있을경우 true값 배정
            if s[x][y] == '!' or s[x][y] == '#':
                a[i][b[x][y]] = True
            x += dx[k]
            y += dy[k]
# bfs로 start문에서 출발해 end문까지의 최소 거울사용 횟수 구함
q = deque()
dist = [-1]*m
q.append(start)
dist[start] = 0
while q:
    # 처음엔 start 값
    now = q.popleft()
    for i in range(m):
        # 연장선상에 거울이 있고, 그 거울을 아직 한번도 방문 하지 않았으면 방문한다
        if a[now][i] != False and dist[i] == -1:
            dist[i] = dist[now]+1
            q.append(i)
# 문이 2개 포함되어있기 때문에 하나 빼준다. 사용한 거울만 들어가야 하므로
print(dist[end]-1)