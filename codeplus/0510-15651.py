# 다시보기
# 브루트포스, 백트래킹
n, m = map(int, input().split())
a = [0]*m

def go(index, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(1, n+1):
        a[index] = i
        go(index+1, n, m)
go(0, n, m)