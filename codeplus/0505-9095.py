# 다이나믹 프로그래밍
T = int(input())
dp = [0]*12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    n = int(input())
    for i in range(4, n+1):
        if dp[i] == 0:
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])