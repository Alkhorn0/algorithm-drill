# 수학, 최대공약수, 최소공배수
a, b = map(int, input().split())
n = min(a, b)
g = 1
for i in range(1, n+1):
    if a % i == 0 and b % i == 0:
        g = max(i, g)
l = a*b//g
print(g)
print(l)