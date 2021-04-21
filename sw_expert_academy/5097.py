T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    for _ in range(m):
        l.append(l.pop(0))
    print(f'#{t} {l[0]}')