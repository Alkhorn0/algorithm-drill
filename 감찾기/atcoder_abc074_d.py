n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    g[i][i] = 10**12

for i in range(n):
    for j in range(i+1, n):
        tmp = 10**12
        for k in range(n):
            tmp = min(tmp, g[i][k]+g[k][j])

        if g[i][j] > tmp:
            print(-1)
            exit()
        elif g[i][j] < tmp:
            ans += g[i][j]
print(ans)