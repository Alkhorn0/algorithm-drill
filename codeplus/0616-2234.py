# 다시보기
# 문제가 총 3개 -> 방의 개수, 가장 넓은 방의 넓이, 벽 한 개를 제거하고 얻는 가장 넓은 방의 크기
# bfs를 통해 각 칸이 어떤 방에 속하는지 구해야 함
# 각 칸의 벽의 배치를 나타내기 위헤 1~15까지의 수 사용(2진수 4자리)
# 좌-> 1(2^0)/ 위-> 2(2^1)/ 우-> 4(2^2)/ 아래-> 8(2^3)

from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 각 칸이 어떤 방에 속하는지 나타냄
d = [[0]*m for _ in range(n)]
def bfs(x, y, rooms):
    q = deque()
    q.append((x, y))
    d[x][y] = rooms
    # 방의 크기 저장
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            # 범위 바깥의 경우 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이미 방문한 칸 제외
            if d[nx][ny] != 0:
                continue
            # 벽으로 막혀있는 쪽으로 이동시 제외
            # k에 맞춰 dx,dy도 세팅해야함
            if (a[x][y] & (1<<k)) > 0:
                continue
            q.append((nx, ny))
            d[nx][ny] = rooms
    return cnt
# 방의 개수 
rooms = 0
# 각 방의 크기
room = [0]
for i in range(n):
    for j in range(m):
        # 방문 안한 칸 -> 새로운 방
        # 방의 개수 +1, 새롭게 bfs하여 방의 크기 구함
        if d[i][j] == 0:
            rooms += 1
            room.append((bfs(i, j, rooms)))
# 문제 1번 방의 개수 출력
print(rooms)
ans = 0
for i in range(1, rooms+1):
    if ans < room[i]:
        ans = room[i]
# 가장 큰 방의 크기
print(ans)
ans = 0
# 벽을 1개 제거시 가장 넓은 방의 크기구하기 위한 연산
for i in range(n):
    for j in range(m):
        x, y = i, j
        # 인접한 칸 쪽의 벽을 제거하여 연결하려함
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            # 범위를 넘어가는 경우 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 같은 방에 속하는 경우, 벽을 제거하는 의미 없음
            # 커지지 않기 때문
            if d[nx][ny] == d[x][y]:
                continue
            # 그 외의 벽이 있는 경우
            # (벽을 1개 제거시 인접한 방 2개가 합쳐지는 경우)
            if (a[x][y] & (1<<k)) > 0:
                # 그 중 가장 큰 경우 선택
                if ans < room[d[x][y]] + room[d[nx][ny]]:
                    ans = room[d[x][y]] + room[d[nx][ny]]
# 마지막 문제의 답
print(ans)