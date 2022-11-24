h, m = map(int, input().split())
while True:
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10

    if 0 <= 10*a+c <= 23 and 0 <= 10*b+d <= 59:
        break
    else:
        if m < 59:
            m += 1
        elif h < 23:
            h += 1
            m = 0
        else:
            h = 0
            m = 0
print(h, m)