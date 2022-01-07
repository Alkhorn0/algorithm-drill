h, w = map(int, input().split())
s = [list(input()) + ['#'] for _ in range(h)] + [['#']*(w+1)]

ud = [[0]*w for _ in range(h)]
for x in range(w+1):
    cnt = 0
    for y in range(h+1):
        if s[y][x] == '#':
            for i in range(cnt):
                ud[y - 1 - i][x] = cnt
            cnt = 0
        else:
            cnt += 1

lr = [[0]*w for _ in range(h)]
for y in range(h+1):
    cnt = 0
    for x in range(w+1):
        if s[y][x] == '#':
            for i in range(cnt):
                lr[y][x - 1 - i] = cnt
            cnt = 0
        else:
            cnt += 1

ans = 0
for y in range(h):
    for x in range(w):
        ans = max(ans, ud[y][x]+lr[y][x]-1)

print(ans)