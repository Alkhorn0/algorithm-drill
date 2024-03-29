# 다시풀기
from copy import deepcopy

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def go(b, t):
    row, col, size = t
    groups = []
    for s in range(1, size+1):
        group = []
        for c in range(col-s, col+s):
            group.append(b[row-s][c])
        for r in range(row-s, row+s):
            group.append(b[r][col+s])
        for c in range(col+s, col-s, -1):
            group.append(b[row+s][c])
        for r in range(row+s, row-s, -1):
            group.append(b[r][col-s])
        groups.append(group)
    for s in range(1, size+1):
        group = groups[s-1]
        group = group[-1:] + group[:-1]
        index = 0
        for c in range(col-s, col+s):
            b[row-s][c] = group[index]
            index += 1
        for r in range(row-s, row+s):
            b[r][col+s] = group[index]
            index += 1
        for c in range(col+s, col-s, -1):
            b[row+s][c] = group[index]
            index += 1
        for r in range(row+s, row-s, -1):
            b[r][col-s] = group[index]
            index += 1


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [list(map(int, input().split())) for _ in range(k)]
d = [(r-1, c-1, s) for r,c,s in d]
d.sort()
ans = 100*100

while True:
    b = deepcopy(a)
    for t in d:
        go(b, t)
    for i in range(n):
        s = sum(b[i])
        if ans > s:
            ans = s
    
    if not next_permutation(d):
        break
print(ans)