# sw 역량 테스트 준비 - 기초 
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = [0]*m
def go(index, n, m):
    if index == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        ans[index] = a[i]
        go(index+1, n, m)
go(0, n, m)