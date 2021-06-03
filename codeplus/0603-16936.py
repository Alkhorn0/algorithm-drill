n = int(input())
b = list(map(int, input().split()))
mul3 = []
div2 = []
check = [False]*len(b)
x = 0
for i in range(len(b)):
    m = b[i]*3
    d = b[i]//2 if b[i]%2 == 0 else -1
    mul3.append(m)
    div2.append(d)
    if m not in b and d not in b:
        x = b[i]
        check[i] = True
a = [x]
while n > 0:
    for i in range(len(b)):
        if check[i]:
            continue
        if a[-1] == mul3[i] or a[-1] == div2[i]:
            a.append(b[i])
            check[i] = True
            break
    n -= 1
print(' '.join(map(str, a)))
