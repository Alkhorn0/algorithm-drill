# brute force, permutation
def next_permutation(a):
    i = k-1
    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = k-1
    while a[j] <= a[i-1]:
        j -= 1
    a[j], a[i-1] = a[i-1], a[j]
    j = k-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

while True:
    k, *s = list(map(int, input().split()))
    if k == 0:
        break
    a = [0]*(k-6)+[1]*6
    ans = []
    while True:
        pos = [s[i] for i in range(k) if a[i] == 1]
        ans.append(pos)
        if not next_permutation(a):
            break
    ans.sort()
    for v in ans:
        print(' '.join(map(str, v)))
    print()
