h, w = map(int, input().split())
s = []
t = []
for _ in range(h):
    s.append(input())
for _ in range(h):
    t.append(input())

ts = [[] for _ in range(w)]
tt = [[] for _ in range(w)]
for i in range(h):
    for j in range(w):
        ts[j].append(s[i][j])
        tt[j].append(t[i][j])

ts = sorted(ts)
tt = sorted(tt)
print('Yes' if ts == tt else 'No')