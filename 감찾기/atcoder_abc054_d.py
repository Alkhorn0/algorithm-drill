inf = 10000000000
n, ma, mb = map(int, input().split())

dp = [[[inf for _ in range(401)] for _ in range(401)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 0

for i in range(n):
    a, b, c = map(int, input().split())
    for ca in range(401):
        for cb in range(401):
            if ca - a >= 0 and cb - b >= 0:
                dp[i+1][ca][cb] = min(dp[i][ca-a][cb-b]+c, dp[i][ca][cb])
            else:
                dp[i+1][ca][cb] = dp[i][ca][cb] 
ans = inf
for ca in range(1, 401):
    for cb in range(1, 401):
        if ca*mb == cb*ma:
            ans = min(ans, dp[-1][ca][cb])

if ans == inf:
    print(-1)
else:
    print(ans)