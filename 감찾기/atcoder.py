from collections import defaultdict
n, q = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(list)

for i in range(n):
    d[a[i]].append(i+1)


for _ in range(q):
    x, k = map(int, input().split())
    if d[x] == []:
        print(-1)
    else:
        t = d[x]
        if len(t) < k:
            print(-1)
        else:
            print(t[k-1])