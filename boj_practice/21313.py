n = int(input())
l = []
if n % 2 != 0:
    for i in range(1, n+1):
        if i % 2 != 0 and i != n:
            l.append(1)
        elif i == n:
            l.append(3)
        else:
            l.append(2)
else:
    for j in range(1, n+1):
        if j % 2 != 0:
            l.append(1)
        else:
            l.append(2)

for k in l:
    print(k, end=' ')
                