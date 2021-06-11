# 투포인터, 브루트포스
n, m = map(int, input().split())
a = list(map(int, input().split()))
left = right = 0
sum = a[0]
ans = 0
while left <= right and right < n:
    if sum < m:
        right += 1
        if right < n:
            sum += a[right]
    elif sum == m:
        ans += 1
        right += 1
        if right < n:
            sum += a[right]
    elif sum > m:
        sum -= a[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = a[left]
print(ans)