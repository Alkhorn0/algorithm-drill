# 그리디 
n, m = map(int, input().split())
miliage = []
for _ in range(n):
    p, l = map(int, input().split())
    miles = list(map(int, input().split()))
    miles.sort(reverse=True)
    if p < l:
        miliage.append(1)
    else:
        if miles[l-1] < 36:
            miliage.append(miles[l-1])
        else:
            miliage.append(36)
miliage.sort()
sum = 0
ans = 0
for i in miliage:
    sum += i
    if sum > m:
        break
    ans += 1
print(ans)
    