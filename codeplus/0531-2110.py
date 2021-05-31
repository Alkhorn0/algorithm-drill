n, c = map(int, input().split())
x = [0]*n
for i in range(n):
    x[i] = int(input())
x.sort()
left = 1
right = x[n-1]-x[0]
ans = 0
def check(x, mid, c):
    a = x[0]
    cnt = 1
    for i in x:
        if i-a >= mid:
            cnt += 1
            a = i
    return cnt >= c

while left <= right:
    mid = (left+right)//2
    if check(x, mid, c):
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1
print(ans)