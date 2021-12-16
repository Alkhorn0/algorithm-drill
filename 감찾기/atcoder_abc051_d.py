n, m = map(int, input().split())
edges = []
dp = [[10**10]*n for _ in range(n)]
# 변 추가
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = c
    dp[b][a] = c
    edges.append((a, b, c))

# 자기루프x
for i in range(n):
    dp[i][i] = 0
# 최단경로 알고리즘 - 워셜 플로이드
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = 0
for i in range(m):
    a, b, c = edges[i]
    if dp[a][b] < c:
        ans += 1
print(ans)        