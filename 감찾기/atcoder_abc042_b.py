n, l = map(int, input().split())
s = list(input() for _ in range(n))

ans = ''
for i in sorted(s):
    ans += i
print(ans)