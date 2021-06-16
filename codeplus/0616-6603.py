# sw 역량 테스트 준비 - 기초
def next_permutation(a):
    i = len(a)-1
    while i >= 0 and a[i] <= a[i-1]:
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

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    a = [0]*(k-6)+[1]*6
    ans = []
    while True:
        temp = [s[i] for i in range(k) if a[i] == 1]
        ans.append(temp)
        if not next_permutation(a):
            break
    ans.sort()
    for i in ans:
        print(' '.join(map(str, i)))
    print()