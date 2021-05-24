# 다시보기
# 가장 가까운 아기상어의 먹잇감을 찾는 함수 -> bfs
# 가장가까운 먹잇감으로 이동해 먹고 위치 갱신 후 이동이 불가할 때까지 반복
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a, x, y, size):
    n = len(a)
    ans = []
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x, y))
    d[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                # ok-> 이동 가능한가/ eat-> 섭취가능한가
                ok = False
                eat = False
                if a[nx][ny] == 0:
                    ok = True
                elif a[nx][ny] < size:
                    ok = True
                    eat = True
                elif a[nx][ny] == size:
                    ok = True
                if ok:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny], nx, ny))
    # 먹을 수 있는 물고기의 존재여부
    if not ans:
        return None
    # 정렬하여 1개만 반환하는 이유는 한번에 한마리씩 아기상어가 먹기 때문에
    ans.sort()
    return ans[0]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0
# 아기상어의 크기
size = 2
# 이동 거리
ans = 0
# 먹은 갯수
exp = 0
while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1
    # 본인 크기만큼 섭취시 아기상어는 커짐
    if size == exp:
        size += 1
        exp = 0
    # 계속된 이동을 위한 크기 갱신
    x, y = nx, ny
print(ans)
