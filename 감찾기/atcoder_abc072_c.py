from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
m = defaultdict(int)
for i in a:
    m[i-1] += 1
    m[i] += 1
    m[i+1] += 1
print(max(m.values()))