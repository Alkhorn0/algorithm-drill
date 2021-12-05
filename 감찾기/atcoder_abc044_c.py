n, a = map(int, input().split())
x = list(int(i)- a for i in input().split())

dp = [[0]*(2*(50*n)+1) for _ in range(0, n+1)]
dp[0][50*n] = 1

for i in range(0, n):
    for j in range(0, 2*50*n+1):
        if dp[i][j] != 0:
            dp[i+1][j] += dp[i][j]
            dp[i+1][x[i]+j] += dp[i][j]

print(dp[n][50*n]-1)