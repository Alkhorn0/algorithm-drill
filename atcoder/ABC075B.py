h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
for i in range(h):
    for j in range(w):
        cnt = 0
        if a[i][j] == '.':
            for k in range(8):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < h and 0 <= ny < w:
                    if a[nx][ny] == '#':
                        cnt += 1
            a[i][j] = cnt
for i in range(h):
    print(''.join(map(str, a[i])))