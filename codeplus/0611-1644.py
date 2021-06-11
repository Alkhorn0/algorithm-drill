# 투포인터, 에라토스테네스의 체
n = int(input())
check = [False]*(n+1)
prime = []
for i in range(2, n+1):
    if check[i]:
        continue
    j = i*2
    prime.append(i)
    while j <= n:
        check[j] = True
        j += i

left = right = 0
sum = 0 if len(prime) == 0 else prime[0]
ans = 0

while left <= right and right < len(prime):
    if sum <= n:
        if sum == n:
            ans += 1
        right += 1
        if right < len(prime):
            sum += prime[right]
    else:
        sum -= prime[left]
        left += 1
print(ans)
