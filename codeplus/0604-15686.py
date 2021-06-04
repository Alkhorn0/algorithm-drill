# 폐점할 가게를 구하는 방법으로 순열을 생각하는 게 중요(못한 부분)

def next_permutaion(d):
    i = len(d)-1
    while i > 0 and d[i-1] >= d[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(d)-1
    while d[j] <= d[i-1]:
        j -= 1
    d[i-1], d[j] = d[j], d[i-1]
    j = len(d)-1
    while i < j:
        d[i], d[j] = d[j], d[i]
        i += 1
        j -= 1
    return True

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            home.append((i, j))
        elif a[i][j] == 2:
            chicken.append((i, j))
d = [0]*len(chicken)
for i in range(m):
    d[i] = 1
d.sort()
ans = -1
while True:
    s = 0
    for r1, c1 in home:
        dists = []
        for i,(r2, c2) in enumerate(chicken):
            if d[i] == 0:
                continue
            dists.append(abs(r1-r2)+abs(c1-c2))
        s += min(dists)
    if ans == -1 or ans > s:
        ans = s 
    if not next_permutaion(d):
        break
print(ans)