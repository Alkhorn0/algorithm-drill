# sw 역량 테스트 준비 - 기초 
n = int(input())
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = i
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i-j*j]+1, dp[i])
        j += 1
print(dp[n])