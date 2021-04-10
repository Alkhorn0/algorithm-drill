n, m = map(int, input().split())
listen = set()
see = set()

for __ in range(n):
    listen.add(input())
for __ in range(m):
    see.add(input())

both = sorted(list(listen & see))
print(len(both))
for i in both:
    print(i)
