# brute force, permutation
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[j], a[i-1] = a[i-1], a[j]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
a = [0]*(n//2)+[1]*(n//2)
ans = 1000
while True:
    start = [i for i in range(n) if a[i] == 0]
    link = [i for i in range(n) if a[i] == 1]
    pos = 0
    for x in range(n//2):
        for y in range(n//2):
            if x != y:
                pos += s[start[x]][start[y]]
                pos -= s[link[x]][link[y]]
    pos = abs(pos)
    ans = min(pos, ans)
    if not next_permutation(a):
        break
print(ans)
