n = int(input())
k = int(input())

left = 1
right = n*n

def check(mid):
    res = 0
    for i in range(1,n+1):
        # 배열의 크기가 n이상 크지 않기 때문에 
        # 더해지는 값도 n이상이 될 수 없음
        res += min(n, mid//i)
    if res >= k:
        return True
    return False
ans = 0
while left <= right:
    mid = (left+right)//2
    if check(mid):
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)