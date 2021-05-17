import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    a = [list(map(int, input().split())) for _ in range(h)]
    g = [[0]*w for _ in range(h)]
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    cnt = 0
    def dfs(x, y, cnt):
        if a[x][y] == 1 and g[x][y] == 0:
            g[x][y] = cnt
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if (0 <= nx < h and 0 <= ny < w):
                    dfs(nx, ny, cnt)
    for x in range(h):
        for y in range(w):
            if a[x][y] == 1 and g[x][y] == 0:
                cnt += 1
                dfs(x, y, cnt)
    print(cnt)