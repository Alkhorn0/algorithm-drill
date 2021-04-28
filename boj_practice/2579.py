# dp문제
n = int(input())
step = [0 for _ in range(301)]
dp = [0 for _ in range(301)] 
for i in range(n):
    step[i] = int(input())
dp[0] = step[0]                 # 첫번째 계단 밟음
dp[1] = step[0] + step[1]       # 두번째 계단 밟는 법중 최대값은 1,2번째 둘다 밟는것
dp[2] = max(step[0] + step[2], step[1] + step[2])   # 1번째 3번째 밟기 or 2,3번째 밟기
# 마지막 계단의 앞계단(i-1)을 밟는 경우 -> 그 전 계단(i-2) 안밟음/ i-1 안 밟는 경우 -> i-2 를 밟아야함
for i in range(3, n):
    dp[i] = max(dp[i-3] + step[i-1]+step[i], dp[i-2] + step[i])

print(dp[n-1])