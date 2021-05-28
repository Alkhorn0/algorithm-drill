# 다시보기
# merge sort, 분할 정복
import sys
input = sys.stdin.readline

def solve(start, end):
    global ans
    mid = (start+end)//2
    if end-start <= 1:
        return
    
    solve(start, mid)
    solve(mid, end)

    b = []
    x, y = start, mid
    cnt = 0
    while x < mid and y < end:
        if a[x] > a[y]:
            b.append(a[y])
            y += 1
            cnt += 1
        else:
            b.append(a[x])
            x += 1
            ans += cnt
    
    while x < mid:
        b.append(a[x])
        x += 1
        ans += cnt
    while y < mid:
        b.append(a[y])
        y += 1
    
    for t in range(len(b)):
        a[start+t] = b[t]

n = int(input())
a = list(map(int, input().split()))
ans = 0
solve(0, n)
print(ans)