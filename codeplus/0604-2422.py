n, m = map(int, input().split())
worst = [[False]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    worst[a-1][b-1] = worst[b-1][a-1] = True
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if worst[i][j] or worst[j][k] or worst[k][i]:
                continue
            ans += 1

print(ans)