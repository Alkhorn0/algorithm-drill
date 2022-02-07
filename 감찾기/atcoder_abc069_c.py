n = int(input())
a = list(map(int, input().split()))
d4, d2, dx = 0, 0, 0
for i in a:
    if i % 4 == 0:
        d4 += 1
    elif i % 2 == 0:
        d2 += 1
    else:
        dx += 1

if d4+1 == dx and n == d4+dx:
    print('Yes')
elif d4 < dx:
    print('No')
else:
    print('Yes')