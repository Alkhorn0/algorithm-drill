k, n = map(int, input().split())
a = [0]*k
for i in range(k):
    a[i] = int(input())
ans = 0
left = 1
right = max(a)
while left <= right:
    mid = (left+right)//2
    x = 0
    for i in range(k):
        x += a[i]//mid
    if x < n:
        right = mid-1
    else:
        ans = mid
        left = mid + 1
print(ans)