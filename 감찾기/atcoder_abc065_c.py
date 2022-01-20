n, m = map(int, input().split())
mod = 10**9+7

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i % mod
    return result

if abs(n-m) >= 2:
    print(0)
elif abs(n-m) == 1:
    print(factorial(n)*factorial(m)%mod)
else:
    print(2*factorial(n)*factorial(m)%mod)