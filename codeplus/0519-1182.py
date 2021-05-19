# bitmask, brute force
n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
# 공집합이 아닌 부분집합 == i (for i in range(1, 1 << n))
for i in range(1, 1<<n):
    sum = 0
    # 부분집합내에 포함되어 있는 지 검사할 요소
    for k in range(n):
        # 존재여부 판정 (존재하면 1/ 존재하지 않으면 0)
        if (i & (1<<k)):
            sum += a[k]
    if sum == s:
        ans += 1
print(ans)