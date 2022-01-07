# 조합에 mod가 나오면 dp를 의심해볼것

n, m = map(int, input().split())
mod = 1000000007
a = []
for _ in range(m):
    a.append(int(input()))

dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
flag = [True]*(n+1)
for i in range(m):
    flag[a[i]] = False

for i in range(n-1):
    if flag[i]:
        dp[i+2] += dp[i]
    if flag[i+1]:
        dp[i+2] += dp[i+1]
    dp[i+2] %= mod

print(dp[n])