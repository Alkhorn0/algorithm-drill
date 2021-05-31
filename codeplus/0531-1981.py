# 다시보기
from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
left = 0
right = 200
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(mn, mx):
    if mn > a[0][0] or mx < a[0][0]:
        return False

    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if mn <= a[nx][ny] and a[nx][ny] <= mx:
                        q.append((nx, ny))
                        visited[nx][ny] = True
    return visited[n-1][n-1]


def go(mid):
    for mn in range(200-mid+1):
        if bfs(mn, mn+mid):
            return True
    return False
ans = 200
while left <= right:
    mid = (left+right)//2
    if go(mid):
        right = mid-1
        ans = min(ans, mid)
    else:
        left = mid+1
print(ans)
    