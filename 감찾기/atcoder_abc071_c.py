from collections import defaultdict

n = int(input())
a = sorted(list(map(int, input().split())))

c = defaultdict(int)
for i in a:
    if c[i] == 0:
        c[i] = 1
    else:
        c[i] += 1

x = []
k = list(c.keys())[::-1]
for i in k:
    if c[i] >= 4:
        x.append(i)
        x.append(i)
    elif c[i] >= 2:
        x.append(i)

if len(x) < 2:
    print(0)
else:
    print(x[0]*x[1])