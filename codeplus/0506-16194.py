# 다이나믹 프로그래밍
n = int(input())
p = list(map(int, input().split()))
dp = [0]*(n+1)
dp[1] = p[0]
for i in range(2, n+1):
    dp[i] = p[i-1]
    for j in range(1, i):
        dp[i] = min(dp[i], dp[j]+dp[i-j])
print(dp[n])