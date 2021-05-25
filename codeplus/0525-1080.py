# greedy
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]

def flip(a, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]
cnt = 0
for x in range(n-2):
    for y in range(m-2):
        if a[x][y] != b[x][y]:
            flip(a, x, y)
            cnt += 1

def check(a, b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

if check(a, b):
    print(cnt)
else:
    print(-1)
