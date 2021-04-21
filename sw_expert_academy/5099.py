T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    ci = list(map(int, input().split()))
    oven = []
    for i in range(n):
        oven.append([i+1, ci[i]])
    i = 0

    while len(oven) != 1:
        oven[0][1] //= 2
        
        if oven[0][1] == 0:
            if n+i < m:
                oven.pop(0)
                oven.append([n+i+1, ci[n+i]])
                i += 1
            elif n+i >= m:
                oven.pop(0)
        else:
            oven.append(oven.pop(0))
    print(f'#{t} {oven[0][0]}')