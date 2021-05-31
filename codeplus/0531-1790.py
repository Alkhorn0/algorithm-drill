n, k = map(int, input().split())

def check(n):
    l = len(str(n))
    res = 0
    start = 1
    for i in range(1, l):
        end = start*10-1
        res += (end-start+1)*i
        start *= 10
    res += (n-start+1)*l
    return res

if check(n) < k:
    print(-1)
else:
    left = 1
    right = n
    ans = 0
    while left <= right:
        mid = (left+right)//2
        length = check(mid)
        if length < k:
            left = mid+1
        else:
            ans = mid
            right = mid-1
    answer = str(ans)
    print(answer[len(answer)-(check(ans)-k)-1])