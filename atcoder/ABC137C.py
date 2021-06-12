from collections import defaultdict
n = int(input())
s = [input() for _ in range(n)]
ans = 0
d = defaultdict(int)
for i in range(n):
    ci = sorted(list(s[i]))
    ci = ''.join(ci)
    ans += d[ci]
    d[ci] += 1
print(ans)