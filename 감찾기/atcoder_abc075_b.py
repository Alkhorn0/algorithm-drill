dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, -1, 0, -1, 1, 0, 1, -1]

h, w = map(int, input().split())
s = list(list(input()) for _ in range(h))

for y in range(h):
    for x in range(w):
        if s[y][x] == '.':
            cnt = 0
            for k in range(8):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < w and 0 <= ny < h:
                    if s[ny][nx] == '#':
                        cnt += 1
            s[y][x] = cnt
for i in range(h):
    print(''.join(map(str, s[i])))