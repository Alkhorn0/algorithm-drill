h, w = map(int, input().split())
n = int(input())
r = [0]*n
c = [0]*n
for i in range(n):
    r[i], c[i] = map(int, input().split())
    
ans = 0
for i in range(n):
    r1, c1 = r[i], c[i]
    for j in range(i+1, n):
        r2, c2 = r[j], c[j]
        for _ in range(2):
            for _ in range(2):
                if r1+r2 <= h and max(c1, c2) <= w:
                    tmp = r1*c1 + r2*c2
                    if ans < tmp:
                        ans = tmp
                if max(r1, r2) <= h and c1+c2 <= w:
                    tmp = r1*c1 + r2*c2
                    if ans < tmp:
                        ans = tmp
                r2, c2 = c2, r2
            r1, c1 = c1, r1
    
print(ans)