# 브루트포스
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
a = [0]*m
v = [False]*n

def go(index, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(n):
        if v[i]:
            continue
        v[i] = True
        a[index] = l[i]
        go(index+1, n, m)
        v[i] = False
go(0, n, m)