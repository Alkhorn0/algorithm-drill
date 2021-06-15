n, k = map(int, input().split())
a = sorted(map(int, input().split()))

s = t = 0
for i in range(n-1, -1, -1):
    if s+a[i] < k:
        s += a[i]
        t += 1
    else:
        t = 0

print(t)