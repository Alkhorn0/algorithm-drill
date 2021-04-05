n, k = map(int,input().split())
coins = []
for __ in range(n):
    coin = int(input())
    coins.append(coin)
result = 0
for i in range(n-1,-1,-1):
    if k // coins[i] != 0:
        result += k // coins[i]
    k = k % coins[i]
    if k == 0:
        break

print(result)