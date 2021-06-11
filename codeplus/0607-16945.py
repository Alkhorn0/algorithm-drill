def check(d):
    magic = d[0]+d[1]+d[2]
    for i in range(3):
        s = 0
        for j in range(3):
            s += d[i*3+j]
        if magic != s:
            return False
    for j in range(3):
        s = 0
        for i in range(3):
            s += d[i*3+j]
        if magic != s:
            return False
    if magic != d[0] + d[4] + d[8]:
        return False
    if magic != d[2] + d[4] + d[6]:
        return False
    return True

def diff (a, d):
    ans = 0
    for i in range(9):
        ans += abs(a[i] - d[i])
    return ans

def next_permutation(d):
    i = len(d)-1
    while i > 0 and d[i-1] >= d[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(d) - 1
    while d[j] <= d[i-1]:
        j -= 1
    d[i-1], d[j] = d[j], d[i-1]
    j = len(d) - 1
    while i < j:
        d[i], d[j] = d[j], d[i]
        i += 1
        j -= 1
    return True

a = []
for i in range(3):
    a += list(map(int, input().split()))
d = list(range(1, 10))
ans = -1

while True:
    if check(d):
        cost = diff(a, d)
        if ans == -1 or ans > cost:
            ans = cost
    if not next_permutation(d):
        break
print(ans)