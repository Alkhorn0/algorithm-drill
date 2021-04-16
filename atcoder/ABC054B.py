n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(input())
b = []
for _ in range(m):
    b.append(input())

for y in range(n-m+1):
    for x in range(n-m+1):
        judge = 0
        for i in range(m):
            if a[y+i][x:x+m] == b[i]:
                judge += 1
        if judge == m:
            print('Yes')
            exit()
print('No')