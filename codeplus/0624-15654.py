# sw 역량 테스트 준비 - 기초 
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
visited = [False]*n
ans = [0]*m

def go(index, n, m):
    if index == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        ans[index] = a[i]
        go(index+1, n, m)
        visited[i] = False
go(0, n, m)
