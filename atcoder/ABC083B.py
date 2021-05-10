n, a, b = map(int, input().split())
l = []
for i in range(1, n+1):
    i = str(i)
    k = 0
    for j in i:
        j = int(j)
        k += j
    if a <= k <= b:
        i = int(i)
        l.append(i)
s = sum(l)
print(s)