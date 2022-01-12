h, w = map(int, input().split())
ans = [list('#' for _ in range(w+2)) for _ in range(h+2)]

a = list(list(input()) for _ in range(h))

for y in range(1, h+1):
    for x in range(1, w+1):
        ans[y][x] = a[y-1][x-1]

for y in range(h+2):
    for x in range(w+2):
        print(ans[y][x],end='')
    print()