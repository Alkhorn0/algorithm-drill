n = int(input())
a = list(map(int, input().split()))
s = sum(a)
ans = 100000000000000000000000000
x = 0

for i in range(n):
    x += a[i]
    if i+1 < n:
        ans = min(ans, abs(s-2*x))

print(ans)