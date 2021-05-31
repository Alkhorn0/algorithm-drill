n, m = map(int, input().split())
t = list(map(int, input().split()))
left = 0
right = 1000000000
ans = 0
while left <= right:
    mid = (left+right)//2
    x = 0
    for i in t:
        if i-mid > 0:
            x += (i-mid)
    if x < m:
        right = mid-1
    else:
        left = mid+1
        ans = mid
print(ans)