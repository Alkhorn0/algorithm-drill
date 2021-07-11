# sw 역량 테스트 준비 - 기초 
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
a = [0]*(n//2)+[1]*(n//2)
ans = 1000000000000000
while next_permutation(a):
    start = []
    link = []
    for i in range(n):
        if a[i] == 0:
            start.append(i)
        else:
            link.append(i)
    start_s = 0
    link_s = 0
    for i in range(n//2):
        for j in range(n//2):
            if i == j:
                continue
            start_s += s[start[i]][start[j]]
            link_s += s[link[i]][link[j]]
    diff = abs(start_s - link_s)
    if ans > diff:
        ans = diff
print(ans)