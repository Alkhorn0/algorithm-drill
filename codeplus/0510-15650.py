# 다른 풀이방식 시도해보기
# 브루트포스, 백트래킹
n, m = map(int, input().split())
c = [False]*(n+1)
a = [0]*m

def per(start, index, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return 
    for i in range(start, n+1):
        if c[i]:
            continue
        c[i] = True
        start = i
        a[index] = i
        per(start, index+1, n, m)
        c[i] = False
per(1, 0, n, m)