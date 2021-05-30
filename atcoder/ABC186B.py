h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
m = a[0][0]
for i in range(h):
    for j in range(w):
        if a[i][j] < m:
            m = a[i][j]

ans = 0
for i in range(h):
    for j in range(w):
        ans += (a[i][j] - m)
print(ans)