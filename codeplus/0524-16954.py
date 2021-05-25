# 다시보기
# 벽이 위에서 내려오기 때문에 t초 전의 상황으로 생각하면 됨
from collections import deque
# 이동할 수 있는 8방향 + 가만히 있는 경우
dx = [1, -1, 0, 0, 1, -1, 1, -1, 0]
dy = [0, 0, 1, -1, 1, -1, -1, 1, 0]
n = 8
a = [input() for _ in range(n)]
q = deque()
check = [[[False]*(n+1) for _ in range(n)] for _ in range(n)]
check[7][0][0] = True
# 시작점이 (7,0)인 이유는 배열의 왼쪽 아래가 시작점이기 때문에 (7행 0열에서부터 시작)
q.append((7, 0, 0))
ans = False

while q:
    x, y, t = q.popleft()
    if x == 0 and y == 7:
        ans = True
    for k in range(9):
        nx, ny = x+dx[k], y+dy[k]
        nt = min(t+1, 8)
        if 0 <= nx < n and 0 <= ny < n:
            # t초 전에 정점에 벽이 있었으면 이동하려는 칸은 벽이므로 이동불가
            if nx-t >= 0 and a[nx-t][ny] == '#':
                continue
            # t+1초전에 정점에 벽이 있었으면 캐릭터가 이동후 바로 벽이 내려오므로 이동불가
            if nx-t-1 >= 0 and a[nx-t-1][ny] == '#':
                continue
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                q.append((nx, ny, nt))
print(1 if ans else 0)