a = list(map(int, input().split()))
ans = [[5, 5, 7], [5, 7, 5], [7, 5, 5]]

if a in ans:
    print('YES')
else:
    print('NO')