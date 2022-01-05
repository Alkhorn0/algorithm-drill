# 다시
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
for _ in range(m):
    b, c = map(int, input().split())
    s = sum(a)
    for i in range(b):
        p = max(s, s+c-sum(a[:i+1]))
        if p == s:
            a = [c]*i + a[i:]
            a.sort()
            break
print(p)

