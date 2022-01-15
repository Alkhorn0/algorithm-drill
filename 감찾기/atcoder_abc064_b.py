n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

ans = a[-1] - a[0]
print(ans)