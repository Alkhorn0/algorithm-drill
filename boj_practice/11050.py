n, k = map(int, input().split())
a, b = 1, 1
for i in range(n, n-k, -1):
    a *= i

for j in range(k, 0, -1):
    b *= j

print(a//b)