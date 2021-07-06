# sw 역량 테스트 준비 - 기초 
mod = 1000000000

n, k = map(int, input().split())
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1

for x in range(1, k+1):
    for y in range(n+1):
        for z in range(y+1):
            dp[x][y] += dp[x-1][y-z]
        dp[x][y] %= mod
print(dp[k][n])
print(dp)