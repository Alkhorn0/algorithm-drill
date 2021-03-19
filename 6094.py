n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

m = a[0]

for i in range(1, n):
    if m >= a[i]:
        m = a[i]

print(m)