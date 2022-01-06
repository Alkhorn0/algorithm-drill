# 비트마스크이용
n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
ans = 0

for bit in range(1<<n):
    on = True
    for i in range(m):
        cnt = 0
        for j in range(ks[i][0]):
            cnt += bit >> (ks[i][j+1]-1) & 1
        if cnt%2 != p[i]:
            on = False
    ans += on
print(ans)