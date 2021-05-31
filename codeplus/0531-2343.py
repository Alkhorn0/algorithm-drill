n, m = map(int, input().split())
a = list(map(int, input().split()))
left = max(a)
right = sum(a)

def check(mid):
    cnt = 1
    s = mid
    for i in range(n):
        s -= a[i]
        if s < 0:
            cnt += 1
            s = mid
            s -= a[i]
    return cnt <= m
ans = 0
while left <= right:
    mid = (left+right)//2
    if check(mid):
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)