# sw 역량 테스트 준비 - 기초
a = sorted([int(input()) for _ in range(9)])
s = sum(a)
for i in range(8):
    s -= a[i]
    ok = False
    for j in range(i+1, 9):
        s -= a[j]
        if s == 100:
            ok = True
            a.remove(a[j])
            break
        s += a[j]
    if ok:
        a.remove(a[i])
        break
    s += a[i]
for i in a:
    print(i)
