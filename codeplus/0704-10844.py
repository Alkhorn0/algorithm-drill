# sw 역량 테스트 준비 - 기초 
mod = 1000000000
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1][0] = 0
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][0] = (dp[i-1][1])%mod
        elif j == 9:
            dp[i][9] = (dp[i-1][8])%mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%mod

print(sum(dp[n])%mod)