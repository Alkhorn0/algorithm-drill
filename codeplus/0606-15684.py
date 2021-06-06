n, m, h = map(int, input().split())
a = [[0]*(n+1) for _ in range(h+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    a[x][y+1] = 2
b = []
for i in range(1, h+1):
    for j in range(1, n):
        if a[i][j] != 0:
            continue
        if a[i][j+1] != 0:
            continue
        b.append((i, j))
ans = -1

def simulate(i):
    r = 1
    while r <= h:
        if a[r][i] == 1:
            i += 1
        elif a[r][i] == 2:
            i -= 1
        r += 1
    return i

def check():
    for i in range(1, n):
        res = simulate(i)
        if res != i:
            return False
    return True

if check():
    print(0)
    exit()
t = len(b)
for i in range(t):
    x1, y1 = b[i]
    if a[x1][y1] != 0 or a[x1][y1+1] != 0:
        continue
    a[x1][y1] = 1
    a[x1][y1+1] = 2
    if check():
        if ans == -1 or ans > 1:
            ans = 1
    for j in range(i+1, t):
        x2, y2 = b[j]
        if a[x2][y2] != 0 or a[x2][y2+1] != 0:
            continue
        a[x2][y2] = 1
        a[x2][y2+1] = 2
        if check():
            if ans == -1 or ans > 3:
                ans = 2
        for k in range(j+1, t):
            x3, y3 = b[k]
            if a[x3][y3] != 0 or a[x3][y3+1] != 0:
                continue
            a[x3][y3] = 1
            a[x3][y3+1] = 2
            if check():
                if ans == -1 or ans > 3:
                    ans = 3
            a[x3][y3] = 0
            a[x3][y3+1] = 0
        a[x2][y2] = 0
        a[x2][y2+1] = 0
    a[x1][y1] = 0
    a[x1][y1+1] = 0
print(ans)