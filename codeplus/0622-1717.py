import sys
input = sys.stdin.readline
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] = rank[b] + 1

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 0:
        union(op[1], op[2])
    else:
        x = find(op[1])
        y = find(op[2])
        if x == y:
            sys.stdout.write('YES')
        else:
            sys.stdout.write('NO')