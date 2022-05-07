n, k = map(int, input().split())
p = []
xi = []
yi = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))
    xi.append(x)
    yi.append(y)

xi.sort()
yi.sort()

ans = (xi[n-1]-xi[0])*(yi[n-1]-yi[0])
for x_i in range(n-1):
    for x_j in range(x_i+1, n):
        for y_i in range(n-1):
            for y_j in range(y_i+1, n):
                cnt = 0
                lx = xi[x_i]
                rx = xi[x_j]
                by = yi[y_i]
                uy = yi[y_j]

                for px, py in p:
                    if lx <= px and px <= rx and by <= py and py <= uy:
                        cnt += 1
                
                if cnt >= k:
                    ans = min(ans, (rx - lx)*(uy - by))
                
print(ans)