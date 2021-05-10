# 브루트포스
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
a = [0]*m

def go(index, s, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(s, n):
        a[index] = l[i]
        s = i
        go(index+1, s, n, m)
go(0, 0, n, m)