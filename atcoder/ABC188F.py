x, y = map(int, input().split())
dp = {}
def go(y):
    if y in dp:
        pass
    elif y == 1:
        dp[y] = abs(x-y)
    elif y%2 == 1:
        dp[y] = min(abs(x-y), go((y-1)//2)+2, go((y+1)//2)+2)
    else:
        dp[y] = min(abs(x-y), go(y//2)+1)
    return dp[y]
print(go(y))