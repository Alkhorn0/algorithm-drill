# 다이나믹 프로그래밍 
x = int(input())
dp = [1000000]*(x+1)
dp[0] ,dp[1] = 0, 0
for i in range(2, x+1):
    possible = []
    if i % 3 == 0:
        possible.append(1+dp[i//3])
    if i % 2 == 0:
        possible.append(1+dp[i//2])
    possible.append(1+dp[i-1])
    dp[i] = min(possible)
print(dp[x])