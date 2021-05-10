# 브루트포스
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
a = [0]*m
d = []

def go(index, n, m):
    if index == m:
        temp = [l[a[i]] for i in range(m)]
        d.append(tuple(temp))
        return
    for i in range(n):
        a[index] = i
        go(index+1, n, m)
go(0, n, m)
d = sorted(list(set(d)))
for j in d:
    print(' '.join(map(str, j)))