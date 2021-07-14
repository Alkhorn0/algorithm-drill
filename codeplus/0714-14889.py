# sw 역량 테스트 준비 - 기초 
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range((1<<n)):
    cnt = 0
    for j in range(n):
        if (i&(1<<j)) > 0:
            cnt += 1
    if cnt != n//2:
        continue
    start = []
    link = []
    for j in range(n):
        if (i&(1<<j)) > 0:
            start += [j]
        else:
            link += [j]
    t1 = 0
    t2 = 0
    for x in range(n//2):
        for y in range(n//2):
            if x == y:
                continue
            t1 += s[start[x]][start[y]]
            t2 += s[link[x]][link[y]]
    diff = abs(t1-t2)
    if ans == -1 or ans > diff:
        ans = diff
print(ans)