# sw 역량 테스트 준비 - 기초 
n = int(input())
a = [0] + [int(input()) for _ in range(n)]
dp = [0]*(n+1)
dp[1] = a[1]
if n >= 2:
    dp[2] = a[1]+a[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+a[i], dp[i-3]+a[i]+a[i-1])

print(dp[n])