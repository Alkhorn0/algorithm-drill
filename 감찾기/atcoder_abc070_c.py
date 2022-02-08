def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

n = int(input())
ans = 1
for _ in range(n):
    t = int(input())
    ans = t*ans//gcd(ans, t)
print(ans)
