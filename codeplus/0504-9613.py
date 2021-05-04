# 수학, 최대공약수, 유클리드 호제법
def uclid(i, j):
    if j == 0:
        return i
    else:
        return uclid(j, i%j)
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    n = l[0]
    gcd = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            gcd.append(uclid(l[i], l[j]))
    print(sum(gcd))