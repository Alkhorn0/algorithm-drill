# 이분 탐색 문제
k, n = map(int, input().split())
lans = []
for __ in range(k):
    lans.append(int(input()))
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lans:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)