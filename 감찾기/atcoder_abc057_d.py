import math

n, a, b = map(int, input().split())
v = sorted(list(map(int, input().split())))

print(sum(v[-a:])/a)
l = v[-a]
c = v.count(l)
d = v[-a:].count(l)

if v[-1] == l:
    ans = sum(math.comb(c, i) for i in range(a, b+1))
else:
    ans = math.comb(c, d)
print(ans)