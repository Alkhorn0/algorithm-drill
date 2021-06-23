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

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

ans = 0
for j in range(2, n+1):
    if find(1) == find(j):
        ans += 1
print(parent)
print(ans)