# 수학, 최대공약수, 유클리드 호제법
def uclid(i, j):
    if j == 0:
        return i
    else:
        return uclid(j, i%j)
n, s = map(int, input().split())
a = list(map(int, input().split()))
d = [0] * n
for i in range(n):
    d[i] = abs(a[i]-s)
gcd = d[0]
for i in range(1, n):
    gcd = uclid(gcd, d[i])
print(gcd)
    