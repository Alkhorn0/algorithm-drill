# 이분탐색 문제 
n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    cut = 0
    for i in range(len(trees)):
        if trees[i] >= mid:
            cut += trees[i] - mid

    if cut >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)