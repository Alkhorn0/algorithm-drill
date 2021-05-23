# 다시보기
# 벽을 3개 두어 가장 큰 안전지역을 만드는 문제, 
# n과 m값이 작기 때문에 둘 수 있는 곳에 
# 벽을 전부 두며 그 때마다  bfs하여 찾는 방식
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            # 처음 바이러스 있는 곳 파악
            if b[i][j] == 2:
                q.append((i, j))
    # 바이러스 확산
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
                b[nx][ny] = 2
                q.append((nx, ny))
    # 안전지역 카운팅
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    # bfs를 통해 안전한 칸 수 반환
    return cnt

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 벽을 둘 수 있는 경우를 하나씩 찾는 것 
# 벽은 3개이므로 6중 for문(2차원)
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0:
                            continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1
                        # 상황마다 bfs
                        cur = bfs(a)
                        if ans < cur:
                            ans = cur
                        # 시험 후 원상복구
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)