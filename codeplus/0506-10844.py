# 다시보기
# 다이나믹 프로그래밍
dp = [[0]*10 for _ in range(100+1)]
mod = 1000000000
n = int(input())
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = 0
        if j-1 >= 0:
            dp[i][j] += dp[i-1][j-1]
        if j+1 <= 9:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= mod
ans = sum(dp[n]) % mod
print(ans)