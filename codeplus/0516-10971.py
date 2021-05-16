# brute force, permutation, Traveling Salesman Problem(TSP)
def next_permutation(a):
    i = n-1
    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = n-1
    while a[j] <= a[i-1]:
        j -= 1
    a[j], a[i-1] = a[i-1], a[j]
    j = n-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
a = [i for i in range(n)]
ans = 1000000000
while True:
    ok = True
    pos = 0
    for i in range(n-1):
        if w[a[i]][a[i+1]] == 0:
            ok = False
            break
        else:
            pos += w[a[i]][a[i+1]]
    if ok and w[a[-1]][a[0]] != 0:
        pos += w[a[-1]][a[0]]
        ans = min(pos, ans)
    if not next_permutation(a):
        break
    # 효율성 개선부분 -> 없으면 시간초과 (한바퀴 돌기 때문에 시작점이 일치해도 무관)
    if a[0] != 0:
        break

print(ans)