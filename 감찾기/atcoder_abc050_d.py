# dp, bitmask
dp = {}
dp[0] = 1
dp[1] = 2
mod = 10**9+7

def df(n):
    if n in dp:
        return dp[n]
    dp[n] = (df(n//2) + df((n-1)//2) + df((n-2)//2)) % mod
    return dp[n]

n = int(input())
print(df(n))
