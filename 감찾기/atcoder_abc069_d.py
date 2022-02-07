h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

color = []
for i, ai in enumerate(a):
    color += [i+1]*ai

ans = [[None]*w for _ in range(h)]
for y in range(h):
    for x in range(w):
        if y % 2 == 1:
            x = -x-1
        ans[y][x] = color.pop()

for y in range(h):
    print(*ans[y])