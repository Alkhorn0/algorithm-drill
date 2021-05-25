# greedy
# 함수에 인자 대입시 원본에도 변화주의 -> a가 아닌 a[:]로 해결
def flipZero(light):
    cnt = 1
    light[0] = 1-light[0]
    light[1] = 1-light[1]
    for i in range(1, n):
        if light[i-1] != b[i-1]:
            cnt += 1
            for j in [i-1, i, i+1]:
                if j >= n:
                    continue
                light[j] = 1-light[j]
    for k in range(n):
        if light[k] != b[k]:
            return 1e10
    return cnt

def noFlipZero(a):
    cnt = 0
    for i in range(1, n):
        if a[i-1] != b[i-1]:
            cnt += 1
            for j in [i-1, i, i+1]:
                if j >= n:
                    continue
                a[j] = 1-a[j]
    for k in range(n):
        if a[k] != b[k]:
            return 1e10
    return cnt

n = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))


ans = 1e10
p1 = flipZero(a[:])
p2 = noFlipZero(a[:])
ans = min(ans, p1, p2)
if ans == 1e10:
    print(-1)
else:
    print(ans)