# permutation, bfs
# 청소기의 이동방법을 순열을 통해 모두 구하고, 그에따른 최소 이동거리를 계산한다

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

# 임의의 두 칸 사이의 최소 이동 거리
# sx, sy -> 초기의 청소기의 위치
def bfs(a, sx, sy):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                # 'x'는 가구를 의미 -> 이동불가 영역
                if dist[nx][ny] == -1 and a[nx][ny] != 'x':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = [input() for _ in range(n)]
    # 청소기 처음좌표 + 청소해야할 좌표 (초기위치는 고정이기 때문에 (0,0)을 미리 대입해둔다)
    b = [(0, 0)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'o':
                b[0] = (i, j)
            elif a[i][j] == '*':
                b.append((i, j))
    # 청소기 위치 + 더러운 칸의 좌표개수
    l = len(b)
    d = [[0]*l for _ in range(l)]
    ok = True
    # 청소기는 초기위치 or 더러운칸 -> 더러운칸 으로 이동 -> 때문에 행렬 b의 크기만큼 for문
    for i in range(l):
        # 청소기의 현재 위치에서 모든 좌표까지의 최소 이동거리
        dist = bfs(a, b[i][0], b[i][1])
        # 현재 위치에서 다음 더러운 칸 까지 최소 이동 거리
        for j in range(l):
            d[i][j] = dist[b[j][0]][b[j][1]]
            # 청소기 청소 못하는 곳이 있다의 의미
            if d[i][j] == -1:
                ok = False
    if not ok:
        print(-1)
        continue
    # 더러운 칸만 이동하면 됨 now = d[0][p[0]] 초기위치는 고정
    # 더러운칸 방문방법(순열)
    p = [i+1 for i in range(l-1)]
    ans = -1
    while True:
        # 처음위치 -> 가장먼저 방문할 더러운 칸
        now = d[0][p[0]]
        for i in range(l-2):
            # 그 다음 이동
            now += d[p[i]][p[i+1]]
        if ans == -1 or ans > now:
            ans = now
        if not next_permutation(p):
            break
    print(ans)