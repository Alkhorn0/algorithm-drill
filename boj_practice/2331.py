a, p = map(int, input().split())
d = [str(a)]
key = 0
while True:
    n = 0
    d_n = d[-1]
    for c in d_n:
        n +=  int(c)**p
    if str(n) in d:
        key = str(n)
        break
    d.append(str(n))
for i in range(len(d)):
    if d[i] == key:
        print(i)
        break