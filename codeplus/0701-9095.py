# sw 역량 테스트 준비 - 기초 
dp = [0]*12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 12):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

t = int(input())
for _ in range(t):
    print(dp[int(input())])