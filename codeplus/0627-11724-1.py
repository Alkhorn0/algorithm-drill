# sw 역량 테스트 준비 - 기초 
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

ans = 0
l = []
for i in range(1, n+1):
    if find(i) not in l:
        ans += 1
        l.append(find(i))

print(ans)