a, b = map(int, input().split())
p = list(str(a))

def prev_permutation(p):
    i = len(p)-1
    while i > 0 and p[i-1] <= p[i]:
        i -= 1
    if i <= 0:
        return -1
    j = len(p)-1
    while p[j] >= p[i-1]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]
    j = len(p)-1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    if p[0] == '0':
        return -1
    else:
        return int(''.join(map(str, p)))

def next_permutation(p):
    i = len(p)-1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    if i <= 0:
        return -1
    j = len(p)-1
    while p[j] <= p[i-1]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]
    j = len(p)-1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    if p[0] == '0':
        return -1
    else:
        return int(''.join(map(str, p)))


if a > b:
    while True:
        c = prev_permutation(p)
        if c <= b or c == -1:
            break
    print(c)
else:
    over = False
    while True:
        c = next_permutation(p)
        if c > b:
            over = True
            break
        elif c == -1:
            break
    if over:
        print(prev_permutation(p))
    else:
        print(int(''.join(map(str, p))))
