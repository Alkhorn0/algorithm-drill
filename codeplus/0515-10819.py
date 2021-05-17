def next_permutation(p):
    i = n-1
    while i > 0 and p[i] <= p[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = n-1
    while p[j] <= p[i-1]:
        j -= 1
    p[j], p[i-1] = p[i-1], p[j]
    j = n-1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
p = [i for i in range(n)]
ans = 0
for i in range(n-1):
    ans += abs(a[p[i]]-a[p[i+1]])
while next_permutation(p):
    pos = 0
    for i in range(n-1):
        pos += abs(a[p[i]]-a[p[i+1]])
    ans = max(ans, pos)
print(ans)